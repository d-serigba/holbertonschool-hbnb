# HBnB - Part 4 Frontend

## Overview

This is the frontend for the HBnB project. It is a static web application that communicates with the HBnB REST API (Part 3 backend) to display places, handle user authentication, and manage reviews.

---

## Prerequisites

- The **Part 3 backend** must be running on `http://127.0.0.1:5000`
- Python 3.10+ with a virtual environment
- A modern web browser (Chrome, Firefox, Edge)

---

## Getting Started

### 1. Start the Backend

```bash
cd ~/holbertonschool-hbnb/part3/hbnb
source ../../venv/bin/activate
python3 run.py
```

The API will be available at `http://127.0.0.1:5000`.

### 2. Start the Frontend Server

Open a **new terminal** and run:

```bash
cd ~/holbertonschool-hbnb/part4
python3 -m http.server 8000
```

### 3. Open the App

Go to: `http://localhost:8000/frontend/index.html`

---

## Test Credentials

| Email | Password | Role |
|-------|----------|------|
| test@test.com | test123 | User |
| admin@hbnb.com | *(see seed.sql)* | Admin |

To create a new user:

```bash
cd ~/holbertonschool-hbnb/part3/hbnb && python3 -c "
from app import create_app
from app.models.base_model import db
from app.models.user import User
app = create_app()
with app.app_context():
    u = User(first_name='Your', last_name='Name', email='you@example.com', password='yourpassword')
    db.session.add(u)
    db.session.commit()
    print('User created!')
"
```

---

## Pages

### `index.html` — List of Places
- Displays all available places as cards with image, description, and price.
- **Filter by price** using the dropdown (10 / 50 / 100 / All).
- The **Login** button is hidden when you are authenticated.
- Click **View Details** to see more about a place.

### `login.html` — Login
- Enter your email and password to authenticate.
- On success, a JWT token is stored in a cookie and you are redirected to the home page.
- An error message is displayed if credentials are invalid.

### `place.html` — Place Details
- Shows full details: title, image, description, price per night, amenities, and reviews.
- Reviews display the reviewer's name, comment, and star rating.
- If you are **logged in**, an **Add Review** button appears.
- Access example: `http://localhost:8000/frontend/place.html?id=<place_id>`

### `add_review.html` — Add a Review
- Only accessible to **authenticated users** — unauthenticated users are redirected to the home page.
- Write a review and select a rating from 1 to 5.
- On success, you are redirected back to the place's detail page.
- Access example: `http://localhost:8000/frontend/add_review.html?id=<place_id>`

---

## Project Structure

```
part4/
└── frontend/
    ├── index.html          # List of places
    ├── login.html          # Login form
    ├── place.html          # Place details + reviews
    ├── add_review.html     # Add review form
    ├── scripts.js          # All JavaScript logic
    ├── styles.css          # Global styles
    └── images/             # Images for each place
        ├── logo.png
        ├── icon.png
        ├── Beach House image
        ├── Mountain Chalet.webp
        ├── modern-urban-loft-stockcake.webp
        ├── Countryside Cottage.webp
        └── Seaside Villa.jpg
```

---

## Authentication Flow

1. User submits email/password on `login.html`
2. Frontend sends a `POST` request to `/auth/login/`
3. On success, the JWT token is stored in a cookie (`token`)
4. All subsequent API requests include the token in the `Authorization: Bearer <token>` header
5. Protected pages (`add_review.html`) check for the cookie on load and redirect if not found

---

## Notes

- The backend must be running for the frontend to work — without it, all API calls will fail.
- Cookies are used for session management (`SameSite=Lax`).
- The price filter works **client-side** — no extra API call is made when filtering.
- A user **cannot review their own place** (enforced by the backend).
- A user **cannot submit two reviews** for the same place.
