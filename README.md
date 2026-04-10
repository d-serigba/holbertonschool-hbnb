# 🏠 HBnB Project — Holberton School AirBnB Clone

> A full-stack AirBnB-inspired web application built across **4 progressive projects**, covering architecture design, REST API development, database persistence, authentication, and frontend integration.

**Authors:** [@d-serigba](https://github.com/d-serigba) & binôme  
**Repository:** [holbertonschool-hbnb](https://github.com/d-serigba/holbertonschool-hbnb/tree/main)

---

## 📚 Table of Contents

- [Overview](#overview)
- [Part 1 — UML & Backend Foundation](#part-1--uml--backend-foundation)
- [Part 2 — Database Persistence with SQLAlchemy](#part-2--database-persistence-with-sqlalchemy)
- [Part 3 — Authentication, Security & Dockerization](#part-3--authentication-security--dockerization)
- [Part 4 — Frontend Client](#part-4--frontend-client)
- [Tech Stack](#tech-stack)
- [Authors](#authors)

---

## Overview

The **HBnB Project** project is a multi-phase software engineering project completed at Holberton School. The goal is to build a simplified clone of AirBnB from the ground up, incrementally adding layers of complexity: from modeling and API design, to persistent storage, secure authentication, and a dynamic frontend.

Each part builds directly on the previous one, simulating a real-world iterative development workflow.

---

## Part 1 — UML & Backend Foundation

> *Architecture design, business logic, in-memory storage, and REST API*

### Objectives

- Design the application's architecture using **UML diagrams** (class diagrams, sequence diagrams, package diagrams)
- Implement the **business logic layer** with a clean separation of concerns
- Build a **RESTful API** using **Flask** and **flask-restx**
- Use an **in-memory repository** as temporary data storage
- Apply the **Facade pattern** to decouple API routes from business logic
- Write comprehensive **unit tests** using `unittest`

### Key Concepts

- Three-layer architecture: Presentation → Business Logic → Persistence
- Models: `User`, `Place`, `Review`, `Amenity` (all inheriting from `BaseModel`)
- CRUD endpoints for all entities
- Input validation and structured error responses

### Structure

```
part1/
├── app/
│   ├── api/          # Flask routes & namespaces
│   ├── models/       # Business logic & entity classes
│   └── services/     # Facade layer
├── tests/            # Unit tests
└── run.py
```

---

## Part 2 — Database Persistence with SQLAlchemy

> *Replacing in-memory storage with a real relational database*

### Objectives

- Integrate **SQLAlchemy ORM** to replace the in-memory repository
- Map all models (`User`, `Place`, `Review`, `Amenity`) to **MySQL** database tables
- Implement **many-to-many relationships** (e.g., Place ↔ Amenity)
- Ensure backward compatibility with the existing API layer
- Use the **repository pattern** with a database-backed implementation

### Key Concepts

- SQLAlchemy declarative models with relationships and cascade operations
- Migration-ready schema with `db.create_all()`
- Environment-based configuration (development / production)
- Data integrity with foreign key constraints

### Structure

```
part2/
├── app/
│   ├── api/
│   ├── models/       # SQLAlchemy-mapped entities
│   ├── persistence/  # DB repository (replaces in-memory)
│   └── services/
├── instance/
│   └── development.db
└── run.py
```

---

## Part 3 — Authentication, Security & Dockerization

> *Securing the API with JWT and containerizing the application*

### Objectives

- Implement **JWT-based authentication** using `flask-jwt-extended`
- Hash passwords securely with **bcrypt**
- Protect API endpoints with authentication and **role-based authorization** (admin vs regular user)
- **Dockerize** the application using an Alpine Linux base image and **Gunicorn** as the WSGI server

### Key Concepts

- Login endpoint returns a signed JWT token
- Protected routes verify tokens on each request
- Admin-only routes enforced via JWT claims
- Docker setup: `Dockerfile`, environment variables, volume for persistent data

### Structure

```
part3/
├── app/
│   ├── api/
│   │   └── auth.py   # Login & protected route decorators
│   ├── models/
│   └── services/
├── Dockerfile
├── requirements.txt
└── wsgi.py
```

### Docker Usage

```bash
# Build the image
docker build -t hbnb .

# Run the container
docker run -d -p 5000:5000 hbnb
```

---

## Part 4 — Frontend Client

> *Building an interactive UI that communicates with the backend API*

### Objectives

- Develop a dynamic frontend using **HTML5**, **CSS3**, and **JavaScript ES6**
- Consume the REST API via the **Fetch API** (AJAX)
- Implement **user authentication** with JWT tokens stored in cookies
- Build the following pages:
  - `index.html` — List of all places with country filter
  - `login.html` — Login form that retrieves and stores a JWT cookie
  - `place.html` — Detailed view of a specific place
  - `add_review.html` — Review form (authenticated users only)
- Redirect unauthenticated users to the login page

### Key Concepts

- Cookie-based session management (JWT stored client-side)
- Client-side filtering without page reloads
- Conditional rendering based on authentication state
- Fetch API with Authorization headers

### Structure

```
part4/
├── index.html
├── login.html
├── place.html
├── add_review.html
├── styles/
│   └── main.css
└── scripts/
    ├── index.js
    ├── login.js
    ├── place.js
    └── add_review.js
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Web Framework | Flask, flask-restx |
| ORM | SQLAlchemy |
| Database | MySQL / SQLite |
| Authentication | JWT (`flask-jwt-extended`), bcrypt |
| Containerization | Docker, Gunicorn |
| Frontend | HTML5, CSS3, JavaScript ES6 |
| Testing | unittest |

---

## Authors

- **Dylan Serigba** — [@d-serigba](https://github.com/d-serigba)
- **David Dufont** — [@dufontdd](https://github.com/dufontdd)

*Project completed at [Holberton School](https://www.holbertonschool.com/) as part of the Higher Level Programming curriculum.*
