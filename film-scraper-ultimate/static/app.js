let basket = [];
let jellyfinLibrary = []; // Films/séries déjà sur Jellyfin

window.addEventListener('DOMContentLoaded', () => {
    loadAll();
});

async function loadAll() {
    await Promise.all([
        loadJellyfinLibrary(),
        loadJellyseerr(),
        loadBasket()
    ]);
}

async function loadJellyfinLibrary() {
    try {
        const response = await fetch('/api/jellyfin/movies');
        const data = await response.json();
        if (data.success && data.movies.length > 0) {
            jellyfinLibrary = data.movies.map(m => m.title.toLowerCase().trim());
            document.getElementById('recentlyAdded').style.display = 'block';
            displayItems('recentlyAddedTrack', data.movies, 'jellyfin');
        }
    } catch (error) {
        console.error('Erreur Jellyfin:', error);
    }
}

async function loadJellyseerr() {
    try {
        // Trending
        const trending = await fetch('/api/jellyseerr/category?category=trending&page=1');
        const trendingData = await trending.json();
        if (trendingData.success) {
            displayItems('trendingTrack', trendingData.items, 'jellyseerr');
        }

        // Popular Movies
        const movies = await fetch('/api/jellyseerr/category?category=movies&page=1');
        const moviesData = await movies.json();
        if (moviesData.success) {
            displayItems('popularMoviesTrack', moviesData.items, 'jellyseerr');
        }

        // Popular Series
        const series = await fetch('/api/jellyseerr/category?category=popular_series&page=1');
        const seriesData = await series.json();
        if (seriesData.success) {
            displayItems('popularSeriesTrack', seriesData.items, 'jellyseerr');
        }

        // Upcoming Movies
        const upcoming = await fetch('/api/jellyseerr/category?category=upcoming&page=1');
        const upcomingData = await upcoming.json();
        if (upcomingData.success) {
            displayItems('upcomingTrack', upcomingData.items, 'jellyseerr');
        }
    } catch (error) {
        console.error('Erreur Jellyseerr:', error);
    }
}

function isInJellyfin(title) {
    const cleanTitle = title.toLowerCase().trim().replace(/[:\-–—]/g, '').replace(/\s+/g, ' ');
    return jellyfinLibrary.some(libTitle => {
        const cleanLibTitle = libTitle.replace(/[:\-–—]/g, '').replace(/\s+/g, ' ');
        return cleanLibTitle === cleanTitle || cleanLibTitle.includes(cleanTitle) || cleanTitle.includes(cleanLibTitle);
    });
}

function displayItems(trackId, items, source) {
    const track = document.getElementById(trackId);
    track.innerHTML = items.map(item => createCard(item, source)).join('');
}

function createCard(item, source) {
    const itemJson = JSON.stringify(item).replace(/"/g, '&quot;');
    const inJellyfin = source === 'jellyseerr' && isInJellyfin(item.title);
    const isSeries = item.media_type === 'tv' || item.title?.includes('Saison');
    const isJellyfinSource = source === 'jellyfin';
    
    return `
        <div class="card ${inJellyfin ? 'in-jellyfin' : ''}">
            ${isSeries ? '<div class="series-badge">SÉRIE</div>' : ''}
            ${inJellyfin ? '<div class="jellyfin-badge">✓</div>' : ''}
            <img src="${item.image || ''}" alt="${item.title}">
            <div class="card-overlay">
                ${!isJellyfinSource && !inJellyfin ? `
                    <button class="card-btn" onclick='addToBasket(${itemJson})' title="Ajouter au panier">
                        <i class="fas fa-heart"></i>
                    </button>
                ` : ''}
                ${!isJellyfinSource && !inJellyfin ? `
                    <button class="card-btn" onclick='searchAndDownload(${itemJson})' title="Rechercher">
                        <i class="fas fa-search"></i>
                    </button>
                ` : ''}
            </div>
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

async function handleSearch(event) {
    if (event.key === 'Enter') {
        const query = event.target.value.trim();
        if (!query) return;
        
        document.getElementById('searchTitle').textContent = `Recherche: ${query}`;
        document.getElementById('searchResults').innerHTML = '<div class="loading"><div class="spinner"></div></div>';
        document.getElementById('searchModal').classList.add('active');
        
        try {
            const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            
            if (data.success && data.films.length > 0) {
                showSearchResults(data.films);
            } else {
                document.getElementById('searchResults').innerHTML = '<p style="text-align:center;color:#94a3b8;">Aucun résultat</p>';
            }
        } catch (error) {
            document.getElementById('searchResults').innerHTML = '<p style="text-align:center;color:#ef4444;">Erreur</p>';
        }
    }
}

function showSearchResults(films) {
    const grid = document.getElementById('searchResults');
    grid.innerHTML = films.map(film => {
        const filmJson = JSON.stringify(film).replace(/"/g, '&quot;');
        return `
            <div class="card">
                <img src="${film.image || ''}" alt="${film.title}">
                <div class="card-overlay">
                    <button class="card-btn" onclick='addToBasket(${filmJson})' title="Ajouter au panier">
                        <i class="fas fa-heart"></i>
                    </button>
                    <button class="card-btn" onclick='openDownload("${film.url}", "${film.title}")' title="Télécharger">
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

async function searchAndDownload(item) {
    const query = item.title;
    document.getElementById('searchTitle').textContent = `Recherche: ${query}`;
    document.getElementById('searchResults').innerHTML = '<div class="loading"><div class="spinner"></div></div>';
    document.getElementById('searchModal').classList.add('active');
    
    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        
        if (data.success && data.films.length > 0) {
            showSearchResults(data.films);
        } else {
            document.getElementById('searchResults').innerHTML = '<p style="text-align:center;color:#94a3b8;">Aucun résultat</p>';
        }
    } catch (error) {
        document.getElementById('searchResults').innerHTML = '<p style="text-align:center;color:#ef4444;">Erreur</p>';
    }
}

async function addToBasket(item) {
    try {
        await fetch('/api/basket/add', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(item)
        });
        loadBasket();
    } catch (error) {
        console.error('Erreur:', error);
    }
}

async function removeFromBasket(item) {
    try {
        await fetch('/api/basket/remove', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(item)
        });
        loadBasket();
    } catch (error) {
        console.error('Erreur:', error);
    }
}

async function loadBasket() {
    try {
        const response = await fetch('/api/basket/list');
        const data = await response.json();
        basket = data.items || [];
        
        const badge = document.getElementById('basketBadge');
        if (basket.length > 0) {
            badge.textContent = basket.length;
            badge.style.display = 'flex';
        } else {
            badge.style.display = 'none';
        }
        
        displayBasket();
    } catch (error) {
        console.error('Erreur:', error);
    }
}

function displayBasket() {
    const content = document.getElementById('basketContent');
    if (basket.length === 0) {
        content.innerHTML = '<p style="text-align:center;color:#64748b;padding:20px;">Panier vide</p>';
        return;
    }
    
    content.innerHTML = basket.map(item => {
        const itemJson = JSON.stringify(item).replace(/"/g, '&quot;');
        return `
            <div class="basket-item">
                <img src="${item.image || ''}" alt="${item.title}">
                <div class="basket-item-info">
                    <div class="basket-item-title">${item.title}</div>
                    <div class="basket-item-meta">${item.year || ''}</div>
                </div>
                <div class="basket-item-actions">
                    <button class="icon-btn" onclick='searchAndDownload(${itemJson})' title="Rechercher">
                        <i class="fas fa-search"></i>
                    </button>
                    <button class="icon-btn" onclick='removeFromBasket(${itemJson})' title="Retirer">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
            </div>
        `;
    }).join('');
}

function toggleBasket() {
    document.getElementById('basketPanel').classList.toggle('active');
}

async function openDownload(url, title) {
    document.getElementById('downloadTitle').textContent = title;
    document.getElementById('downloadOptions').innerHTML = '<div class="loading"><div class="spinner"></div><p>Extraction...</p></div>';
    document.getElementById('downloadModal').classList.add('active');
    
    try {
        const response = await fetch(`/api/download-links?url=${encodeURIComponent(url)}`);
        const data = await response.json();
        const options = document.getElementById('downloadOptions');
        
        if (data.success && data.links) {
            const hasLinks = data.links.truefrench || data.links.french || data.links.vostfr;
            if (hasLinks) {
                options.innerHTML = `<div class="download-options">
                    ${data.links.truefrench ? `<a href="${data.links.truefrench}" class="download-option" download="${title}_TRUEFRENCH.mp4">🇫🇷 TRUEFRENCH</a>` : ''}
                    ${data.links.french ? `<a href="${data.links.french}" class="download-option" download="${title}_FRENCH.mp4">🇫🇷 FRENCH</a>` : ''}
                    ${data.links.vostfr ? `<a href="${data.links.vostfr}" class="download-option" download="${title}_VOSTFR.mp4">🇬🇧 VOSTFR</a>` : ''}
                </div>`;
            } else {
                options.innerHTML = '<p style="text-align:center;color:#94a3b8;">Aucun lien disponible</p>';
            }
        } else {
            options.innerHTML = '<p style="text-align:center;color:#94a3b8;">Aucun lien disponible</p>';
        }
    } catch (error) {
        document.getElementById('downloadOptions').innerHTML = '<p style="text-align:center;color:#ef4444;">Erreur</p>';
    }
}

function closeDownloadModal() {
    document.getElementById('downloadModal').classList.remove('active');
}

function closeSearchModal() {
    document.getElementById('searchModal').classList.remove('active');
}

function openSettings() {
    document.getElementById('settingsModal').classList.add('active');
}

function closeSettings() {
    document.getElementById('settingsModal').classList.remove('active');
}

function switchTab(tab) {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    event.target.classList.add('active');
    document.getElementById(`${tab}-tab`).classList.add('active');
}

async function saveJellyfin() {
    const url = document.getElementById('jellyfinUrl').value;
    const apiKey = document.getElementById('jellyfinApiKey').value;
    
    try {
        const response = await fetch('/api/jellyfin/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({url, api_key: apiKey})
        });
        const data = await response.json();
        document.getElementById('jellyfinStatus').innerHTML = data.success ? 
            `<p style="color:#10b981;">✓ Connecté (${data.count} films)</p>` : 
            '<p style="color:#ef4444;">✗ Échec</p>';
        
        if (data.success) setTimeout(() => location.reload(), 1000);
    } catch (error) {
        document.getElementById('jellyfinStatus').innerHTML = '<p style="color:#ef4444;">✗ Erreur</p>';
    }
}

async function saveJellyseerr() {
    const url = document.getElementById('jellyseerrUrl').value;
    const apiKey = document.getElementById('jellyseerrApiKey').value;
    
    try {
        const response = await fetch('/api/jellyseerr/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({url, api_key: apiKey})
        });
        const data = await response.json();
        document.getElementById('jellyseerrStatus').innerHTML = data.success ? 
            '<p style="color:#10b981;">✓ Connecté</p>' : 
            '<p style="color:#ef4444;">✗ Échec</p>';
        
        if (data.success) setTimeout(() => location.reload(), 1000);
    } catch (error) {
        document.getElementById('jellyseerrStatus').innerHTML = '<p style="color:#ef4444;">✗ Erreur</p>';
    }
}

async function saveStreamingUrl() {
    const url = document.getElementById('streamingUrl').value;
    
    try {
        const response = await fetch('/api/streaming/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({url})
        });
        const data = await response.json();
        document.getElementById('streamingStatus').innerHTML = data.success ? 
            '<p style="color:#10b981;">✓ Enregistré</p>' : 
            '<p style="color:#ef4444;">✗ Erreur</p>';
    } catch (error) {
        document.getElementById('streamingStatus').innerHTML = '<p style="color:#ef4444;">✗ Erreur</p>';
    }
}

function navigateToGenre(genre) {
    window.location.href = `/discover/${genre}`;
}

function navigateToStudio(studioId) {
    window.location.href = `/discover/studio_${studioId}`;
}

function navigateToNetwork(networkId) {
    window.location.href = `/discover/network_${networkId}`;
}
