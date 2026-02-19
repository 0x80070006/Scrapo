let currentPage = 1;
let loading = false;
let hasMore = true;
let category = '';
let jellyfinLibrary = [];

window.addEventListener('DOMContentLoaded', async () => {
    // Charger la bibliothèque Jellyfin
    await loadJellyfinLibrary();
    
    // Extraire la catégorie depuis l'URL
    const path = window.location.pathname;
    category = path.split('/').pop();
    
    // Mettre à jour le titre
    const titles = {
        'trending': 'Trending',
        'movies': 'Popular Movies',
        'series': 'Popular Series',
        'popular_series': 'Popular Series',
        'upcoming': 'Upcoming Movies',
        'action': 'Action Movies',
        'comedy': 'Comedy Movies',
        'drama': 'Drama Movies',
        'horror': 'Horror Movies',
        'scifi': 'Science Fiction Movies',
        'thriller': 'Thriller Movies',
        'action_series': 'Action Series',
        'comedy_series': 'Comedy Series',
        'drama_series': 'Drama Series',
        'scifi_series': 'Sci-Fi Series',
        'mystery_series': 'Mystery Series',
        'animation_series': 'Animation Series',
        // Studios
        'studio_2': 'Disney',
        'studio_127928': '20th Century Studios',
        'studio_34': 'Sony Pictures',
        'studio_174': 'Warner Bros.',
        'studio_33': 'Universal',
        'studio_4': 'Paramount',
        'studio_3': 'Pixar',
        'studio_521': 'DreamWorks',
        'studio_420': 'Marvel Studios',
        'studio_9993': 'DC',
        'studio_41077': 'A24',
        // Networks
        'network_213': 'Netflix',
        'network_2739': 'Disney+',
        'network_1024': 'Amazon Prime Video',
        'network_453': 'Hulu',
        'network_2552': 'Apple TV+',
        'network_3353': 'Peacock'
    };
    document.getElementById('discoverTitle').textContent = titles[category] || 'Discover';
    
    // Charger la première page
    loadMore();
    
    // Activer le scroll infini
    window.addEventListener('scroll', handleScroll);
});

async function loadJellyfinLibrary() {
    try {
        const response = await fetch('/api/jellyfin/movies');
        const data = await response.json();
        if (data.success && data.movies.length > 0) {
            jellyfinLibrary = data.movies.map(m => m.title.toLowerCase().trim());
        }
    } catch (error) {
        console.error('Erreur Jellyfin:', error);
    }
}

function isInJellyfin(title) {
    const cleanTitle = title.toLowerCase().trim().replace(/[:\-–—]/g, '').replace(/\s+/g, ' ');
    return jellyfinLibrary.some(libTitle => {
        const cleanLibTitle = libTitle.replace(/[:\-–—]/g, '').replace(/\s+/g, ' ');
        return cleanLibTitle === cleanTitle || cleanLibTitle.includes(cleanTitle) || cleanTitle.includes(cleanLibTitle);
    });
}

function handleScroll() {
    if (loading || !hasMore) return;
    
    // Détecter la position du scroll
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight;
    const clientHeight = window.innerHeight;
    
    // Charger plus quand on arrive à 80% du scroll (comme Jellyseerr)
    if (scrollTop + clientHeight >= scrollHeight - 200) {
        console.log('🔄 Scroll détecté - Chargement page', currentPage);
        loadMore();
    }
}

async function loadMore() {
    if (loading || !hasMore) return;
    
    loading = true;
    document.getElementById('loading').style.display = 'block';
    
    console.log(`📥 Chargement page ${currentPage} pour ${category}`);
    
    try {
        const response = await fetch(`/api/jellyseerr/category?category=${category}&page=${currentPage}`);
        const data = await response.json();
        
        if (data.success && data.items && data.items.length > 0) {
            console.log(`✅ ${data.items.length} items reçus`);
            displayItems(data.items);
            currentPage++;
        } else {
            console.log('❌ Plus de résultats');
            hasMore = false;
        }
    } catch (error) {
        console.error('Erreur:', error);
        hasMore = false;
    } finally {
        loading = false;
        document.getElementById('loading').style.display = 'none';
    }
}

function displayItems(items) {
    const grid = document.getElementById('discoverGrid');
    items.forEach(item => {
        const card = createCard(item);
        grid.insertAdjacentHTML('beforeend', card);
    });
}

function createCard(item) {
    const itemJson = JSON.stringify(item).replace(/"/g, '&quot;');
    const inJellyfin = isInJellyfin(item.title);
    const isSeries = item.media_type === 'tv' || item.title?.includes('Saison');
    
    return `
        <div class="card ${inJellyfin ? 'in-jellyfin' : ''}">
            ${isSeries ? '<div class="series-badge">SÉRIE</div>' : ''}
            ${inJellyfin ? '<div class="jellyfin-badge">✓</div>' : ''}
            <img src="${item.image || ''}" alt="${item.title}" loading="lazy">
            ${!inJellyfin ? `
                <div class="card-overlay">
                    <button class="card-btn" onclick='addToBasket(${itemJson})' title="Ajouter au panier">
                        <i class="fas fa-heart"></i>
                    </button>
                    <button class="card-btn" onclick='searchAndDownload(${itemJson})' title="Rechercher">
                        <i class="fas fa-search"></i>
                    </button>
                </div>
            ` : ''}
            <div class="card-info">
                <div class="card-title">${item.title}</div>
                <div class="card-meta">
                    ${item.year ? item.year : ''}
                    ${item.rating ? ` • ⭐ ${item.rating.toFixed(1)}` : ''}
                </div>
            </div>
        </div>
    `;
}

async function addToBasket(item) {
    try {
        await fetch('/api/basket/add', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(item)
        });
        alert('✅ Ajouté au panier !');
    } catch (error) {
        console.error('Erreur:', error);
    }
}

async function searchAndDownload(item) {
    const query = item.title;
    
    // Ouvrir modal de recherche
    const searchModal = window.parent.document.getElementById('searchModal');
    const searchTitle = window.parent.document.getElementById('searchTitle');
    const searchResults = window.parent.document.getElementById('searchResults');
    
    if (!searchModal) {
        alert('Fonctionnalité de recherche non disponible sur cette page');
        return;
    }
    
    searchTitle.textContent = `Recherche: ${query}`;
    searchResults.innerHTML = '<div class="loading"><div class="spinner"></div></div>';
    searchModal.classList.add('active');
    
    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        
        if (data.success && data.films.length > 0) {
            showSearchResults(data.films, searchResults);
        } else {
            searchResults.innerHTML = '<p style="text-align:center;color:#94a3b8;">Aucun résultat</p>';
        }
    } catch (error) {
        searchResults.innerHTML = '<p style="text-align:center;color:#ef4444;">Erreur</p>';
    }
}

function showSearchResults(films, container) {
    container.innerHTML = films.map(film => {
        const filmJson = JSON.stringify(film).replace(/"/g, '&quot;');
        return `
            <div class="card">
                <img src="${film.image || ''}" alt="${film.title}">
                <div class="card-overlay">
                    <button class="card-btn" onclick='window.parent.openDownload("${film.url}", "${film.title}")' title="Télécharger">
                        <i class="fas fa-download"></i>
                    </button>
                </div>
                <div class="card-info">
                    <div class="card-title">${film.title}</div>
                    <div class="card-meta">${film.year || ''}</div>
                </div>
            </div>
        `;
    }).join('');
}
