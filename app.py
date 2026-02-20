from flask import Flask, render_template, jsonify, request
from scraper import FilmScraper
import requests
import re

app = Flask(__name__)
app.secret_key = 'ultimate-scraper-secret'

scraper_instance = None
jellyfin_settings = {}
jellyseerr_settings = {}
streaming_settings = {'url': 'https://fs9.lol'}
basket = []

def get_scraper():
    global scraper_instance
    if scraper_instance is None:
        base_url = streaming_settings.get('url', 'https://fs9.lol')
        scraper_instance = FilmScraper(headless=True, base_url=base_url)
    return scraper_instance

def get_jellyfin_movies():
    if not jellyfin_settings.get('url') or not jellyfin_settings.get('api_key'):
        return []
    try:
        url = jellyfin_settings['url'].rstrip('/')
        api_key = jellyfin_settings['api_key']
        response = requests.get(
            f"{url}/Items",
            params={'IncludeItemTypes': 'Movie', 'Recursive': 'true', 'Fields': 'Name,PremiereDate,CommunityRating'},
            headers={'X-Emby-Token': api_key},
            timeout=10
        )
        if response.status_code == 200:
            movies = []
            for item in response.json().get('Items', []):
                movies.append({
                    'title': item.get('Name', ''),
                    'year': item.get('PremiereDate', '')[:4] if item.get('PremiereDate') else '',
                    'rating': item.get('CommunityRating', 0),
                    'image': f"{url}/Items/{item['Id']}/Images/Primary?api_key={api_key}",
                    'id': item.get('Id')
                })
            return movies
    except: pass
    return []

def get_jellyseerr_data(page=1, category='movies'):
    if not jellyseerr_settings.get('url') or not jellyseerr_settings.get('api_key'):
        return []
    try:
        url = jellyseerr_settings['url'].rstrip('/')
        api_key = jellyseerr_settings['api_key']
        headers = {'X-Api-Key': api_key}
        
        # Mapping des catégories vers les endpoints Jellyseerr
        endpoints = {
            'movies': '/api/v1/discover/movies',
            'series': '/api/v1/discover/tv',
            'trending': '/api/v1/discover/trending',
            'upcoming': '/api/v1/discover/movies/upcoming',
            'popular_series': '/api/v1/discover/tv',
            # Genres films
            'action': '/api/v1/discover/movies/genre/28',
            'comedy': '/api/v1/discover/movies/genre/35',
            'drama': '/api/v1/discover/movies/genre/18',
            'horror': '/api/v1/discover/movies/genre/27',
            'scifi': '/api/v1/discover/movies/genre/878',
            'thriller': '/api/v1/discover/movies/genre/53',
            # Genres séries
            'action_series': '/api/v1/discover/tv/genre/10759',
            'comedy_series': '/api/v1/discover/tv/genre/35',
            'drama_series': '/api/v1/discover/tv/genre/18',
            'scifi_series': '/api/v1/discover/tv/genre/10765',
            'mystery_series': '/api/v1/discover/tv/genre/9648',
            'animation_series': '/api/v1/discover/tv/genre/16'
        }
        
        # Gestion dynamique des studios : studio_420 -> /discover/movies/company/420
        if category.startswith('studio_'):
            studio_id = category.replace('studio_', '')
            endpoint = f'/api/v1/discover/movies/company/{studio_id}'
        # Gestion dynamique des networks : network_213 -> /discover/tv/network/213
        elif category.startswith('network_'):
            network_id = category.replace('network_', '')
            endpoint = f'/api/v1/discover/tv/network/{network_id}'
        else:
            endpoint = endpoints.get(category, endpoints['movies'])
        
        resp = requests.get(f"{url}{endpoint}", headers=headers, params={'page': page}, timeout=10)
        
        if resp.status_code == 200:
            results = []
            for item in resp.json().get('results', []):
                results.append({
                    'title': item.get('title') or item.get('name', ''),
                    'year': (item.get('releaseDate') or item.get('firstAirDate', ''))[:4] if (item.get('releaseDate') or item.get('firstAirDate')) else '',
                    'rating': item.get('voteAverage', 0),
                    'image': f"https://image.tmdb.org/t/p/w500{item.get('posterPath')}" if item.get('posterPath') else '',
                    'overview': item.get('overview', ''),
                    'tmdb_id': item.get('id'),
                    'media_type': item.get('media_type', 'tv' if 'name' in item else 'movie')
                })
            return results
    except Exception as e:
        print(f"Error fetching Jellyseerr: {e}")
    return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/discover/<category>')
def discover(category):
    return render_template('discover.html', category=category)

@app.route('/api/jellyfin/movies')
def get_jellyfin_movies_api():
    return jsonify({'success': True, 'movies': get_jellyfin_movies()})

@app.route('/api/jellyseerr/category')
def get_jellyseerr_category():
    category = request.args.get('category', 'movies')
    page = int(request.args.get('page', 1))
    data = get_jellyseerr_data(page, category)
    return jsonify({'success': True, 'items': data, 'page': page})

@app.route('/api/search')
def search_films():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({'success': False}), 400
    scraper = get_scraper()
    search_url = f"/index.php?do=search&subaction=search&story={query}"
    all_films = []
    for page in range(1, 4):
        films = scraper.get_films_from_page(page, base_url=search_url)
        if not films:
            break
        all_films.extend(films)
    return jsonify({'success': True, 'films': all_films})

@app.route('/api/download-links')
def get_download_links():
    film_url = request.args.get('url')
    if not film_url:
        return jsonify({'success': False}), 400
    scraper = get_scraper()
    links = scraper.get_download_links(film_url)
    if links and any(links.values()):
        return jsonify({'success': True, 'links': links})
    return jsonify({'success': False}), 404

@app.route('/api/basket/add', methods=['POST'])
def add_to_basket():
    global basket
    data = request.json
    for item in basket:
        if (item.get('title') == data.get('title')) or \
           (item.get('tmdb_id') and item.get('tmdb_id') == data.get('tmdb_id')):
            return jsonify({'success': False})
    basket.append(data)
    return jsonify({'success': True})

@app.route('/api/basket/list')
def list_basket():
    return jsonify({'success': True, 'items': basket})

@app.route('/api/basket/remove', methods=['POST'])
def remove_from_basket():
    global basket
    data = request.json
    title = data.get('title')
    tmdb_id = data.get('tmdb_id')
    basket = [item for item in basket if not (
        (item.get('title') == title) or 
        (item.get('tmdb_id') and item.get('tmdb_id') == tmdb_id)
    )]
    return jsonify({'success': True})

@app.route('/api/jellyfin/test', methods=['POST'])
def test_jellyfin():
    data = request.json
    url = data.get('url', '').rstrip('/')
    api_key = data.get('api_key')
    try:
        response = requests.get(f"{url}/System/Info", headers={'X-Emby-Token': api_key}, timeout=5)
        if response.status_code == 200:
            return jsonify({'success': True})
    except: pass
    return jsonify({'success': False, 'error': 'Connexion échouée'})

@app.route('/api/jellyfin/save', methods=['POST'])
def save_jellyfin():
    global jellyfin_settings
    data = request.json
    jellyfin_settings = {'url': data.get('url', '').rstrip('/'), 'api_key': data.get('api_key')}
    movies = get_jellyfin_movies()
    return jsonify({'success': True, 'count': len(movies)})

@app.route('/api/jellyseerr/test', methods=['POST'])
def test_jellyseerr():
    data = request.json
    url = data.get('url', '').rstrip('/')
    api_key = data.get('api_key')
    try:
        response = requests.get(f"{url}/api/v1/settings/public", headers={'X-Api-Key': api_key}, timeout=5)
        if response.status_code == 200:
            return jsonify({'success': True})
    except: pass
    return jsonify({'success': False, 'error': 'Connexion échouée'})

@app.route('/api/jellyseerr/save', methods=['POST'])
def save_jellyseerr():
    global jellyseerr_settings
    data = request.json
    jellyseerr_settings = {'url': data.get('url', '').rstrip('/'), 'api_key': data.get('api_key')}
    return jsonify({'success': True})

@app.route('/api/streaming/save', methods=['POST'])
def save_streaming_url():
    global streaming_settings, scraper_instance
    data = request.json
    streaming_settings['url'] = data.get('url', '').rstrip('/')
    scraper_instance = None
    return jsonify({'success': True})

@app.route('/api/streaming/settings')
def get_streaming_settings():
    return jsonify({'success': True, 'url': streaming_settings.get('url', 'https://fs9.lol')})

if __name__ == '__main__':
    print("🚀 Film Scraper Ultimate")
    print("📍 http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
