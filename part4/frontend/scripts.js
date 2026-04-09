document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.pathname;

    if (path.includes('index.html') || path === '/' || path === '/index.html') {
        initIndexPage();
    } else if (path.includes('place.html')) {
        initPlacePage();
    } else if (path.includes('add_review.html')) {
        initAddReviewPage();
    } else if (path.includes('login.html')) {
        initLoginPage();
    }
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function checkAuthentication() {
    const token = getCookie('token');
    if (!token) {
        window.location.href = 'index.html';
    }
    return token;
}

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

function getPlaceImage(title) {
    const images = {
        'Beach House': 'images/illustration-du-lever-du-soleil-maison-plage_1371855-7723.avif',
        'Mountain Chalet': 'images/Mountain Chalet.webp',
        'City Loft': 'images/modern-urban-loft-stockcake.webp',
        'Countryside Cottage': 'images/Countryside Cottage.webp',
        'Seaside Villa': 'images/Seaside Villa.jpg',
    };
    return images[title] || 'images/img_index.png';
}

function initLoginPage() {
    const loginForm = document.getElementById('login-form');
    if (!loginForm) return;

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        try {
            const response = await fetch('http://127.0.0.1:5000/auth/login/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            if (response.ok) {
                const data = await response.json();
                document.cookie = `token=${data.access_token}; path=/; SameSite=Lax`;
                window.location.href = 'index.html';
            } else {
                document.getElementById('error-message').textContent = 'Login failed: wrong email or password';
            }
        } catch (error) {
            document.getElementById('error-message').textContent = 'Server error';
        }
    });
}

async function initIndexPage() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (loginLink) {
        loginLink.style.display = token ? 'none' : 'block';
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/places/', {
            headers: token ? { 'Authorization': `Bearer ${token}` } : {}
        });
        const places = await response.json();
        displayPlaces(places);
    } catch (err) {
        document.getElementById('places-list').innerHTML = 'Server error';
    }

    const filter = document.getElementById('price-filter');
    if (filter) filter.addEventListener('change', filterPlaces);
}

function displayPlaces(places) {
    const container = document.getElementById('places-list');
    container.innerHTML = '';

    places.forEach(place => {
        const card = document.createElement('div');
        card.className = 'place-card';
        card.setAttribute('data-price', place.price);

        card.innerHTML = `
            <img src="${getPlaceImage(place.title)}" alt="${place.title}" class="place-thumb">
            <div class="place-info">
                <h2>${place.title}</h2>
                <p>${place.description || 'No description'}</p>
                <p class="price-tag">$${place.price}/night</p>
                <a class="details-button" href="place.html?id=${place.id}">View Details</a>
            </div>
        `;
        container.appendChild(card);
    });
}

function filterPlaces(e) {
    const value = e.target.value;
    const cards = document.querySelectorAll('.place-card');
    cards.forEach(card => {
        const price = parseInt(card.getAttribute('data-price'));
        card.style.display = (value === 'All' || price <= parseInt(value)) ? 'flex' : 'none';
    });
}

async function initPlacePage() {
    const token = getCookie('token');
    const placeId = getPlaceIdFromURL();

    if (!placeId) {
        window.location.href = 'index.html';
        return;
    }

    const loginLink = document.getElementById('login-link');
    if (loginLink) {
        loginLink.style.display = token ? 'none' : 'block';
    }

    await fetchPlaceDetails(token, placeId);
}

async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/places/${placeId}/`, {
            headers: token ? { 'Authorization': `Bearer ${token}` } : {}
        });
        const place = await response.json();
        displayPlaceDetails(place);
    } catch (err) {
        document.getElementById('place-details').innerHTML = 'Failed to load place';
    }
}

function displayPlaceDetails(place) {
    const container = document.getElementById('place-details');
    container.innerHTML = `
        <div class="place-details-content">
            <h1>${place.title}</h1>
            <img src="${getPlaceImage(place.title)}" class="main-image" alt="${place.title}">
            <div class="place-info-box">
                <p><strong>Description:</strong> ${place.description || 'No description'}</p>
                <p><strong>Price:</strong> $${place.price}/night</p>
                <p><strong>Amenities:</strong> ${place.amenities && place.amenities.length ? place.amenities.join(', ') : 'None'}</p>
            </div>
            <hr>
            <h2>Reviews:</h2>
            <div class="reviews-list">
                ${place.reviews && place.reviews.length
                    ? place.reviews.map(r => `
                        <div class="review-card">
                            <p><strong>${r.user || 'Anonymous'}:</strong> ${r.text}</p>
                            <p>Rating: ${'★'.repeat(r.rating)}${'☆'.repeat(5 - r.rating)}</p>
                        </div>`).join('')
                    : '<p>No reviews yet</p>'}
            </div>
        </div>
    `;

    const token = getCookie('token');
    const reviewContainer = document.getElementById('add-review-container');
    if (token) {
        reviewContainer.innerHTML = `<a href="add_review.html?id=${place.id}" class="details-button">Add Review</a>`;
    } else {
        reviewContainer.innerHTML = `<p><a href="login.html">Login</a> to add a review.</p>`;
    }
}

function initAddReviewPage() {
    const token = checkAuthentication();
    const placeId = getPlaceIdFromURL();
    const reviewForm = document.getElementById('review-form');

    if (!reviewForm) return;

    reviewForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = document.getElementById('review-text').value;
        const rating = document.getElementById('review-rating').value;

        try {
            const response = await fetch('http://127.0.0.1:5000/reviews/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    place_id: placeId,
                    text: text,
                    rating: parseInt(rating)
                })
            });

            if (response.ok) {
                alert('Review submitted successfully!');
                window.location.href = `place.html?id=${placeId}`;
            } else {
                const err = await response.json();
                document.getElementById('review-error').textContent = err.message || 'Failed to submit review';
            }
        } catch (err) {
            document.getElementById('review-error').textContent = 'Server or CORS error';
        }
    });
}
