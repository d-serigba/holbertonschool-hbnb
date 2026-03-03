# HBnB Project - Part 2: RESTful API Implementation

## 📖 Project Overview

This stage of the HBnB project focuses on building the core business logic and exposing it through a RESTful API. The system manages property listings, user profiles, customer reviews, and amenities. It is built with a focus on **scalability**, **data integrity**, and a **clean architecture**.

## 🏗️ Technical Architecture

The application follows a **Layered Architecture** to ensure a clear separation of concerns:

1.  **Presentation Layer (API)**: Handles HTTP requests and responses using Flask-RESTx.
    
2.  **Business Logic Layer (Services/Facade)**: Coordinates actions between models and persistence, ensuring the API never interacts directly with the data storage.
    
3.  **Persistence Layer (Repository)**: Manages data storage (currently In-Memory).
    
4.  **Model Layer**: Defines the core entities (User, Place, Review, Amenity) and their relationships.

## ✨ Core Features

-   **User Management**: Create and retrieve user profiles with unique email validation.
    
-   **Property Listings (Places)**: Manage properties, including pricing, coordinates, and owner associations (1:1 Relationship).
    
-   **Amenity System**: Manage property features (e.g., WiFi, Parking) and link them to specific places (Many-to-Many Relationship).
    
-   **Review System**: Implement customer feedback with full CRUD capabilities, including a secure **DELETE** operation.

## Testing & Validation

Quality assurance is a priority. We implemented strict validation rules and automated tests to ensure the system is reliable.

### Data Validation

The API enforces several business rules to prevent invalid data entry:

-   **Ratings**: Must be an integer between 1 and 5.
    
-   **Pricing**: Negative prices are strictly rejected.
    
-   **Coordinates**: Latitude and Longitude must be within valid geographical ranges.
    

### Automated Unit Tests

A dedicated testing suite was developed to simulate real-world usage and edge cases. **Latest Test Execution Results:**

`(venv) d-serigba@N14C-4BK128:~/holbertonschool-hbnb/part2$ export PYTHONPATH=. && python3 -m unittest discover tests`
`..`
`----------------------------------------------------------------------`
`Ran 2 tests in 0.069s`

`OK`

Result: All core services passed the integrity check.

## 🛠️ Installation and Setup
1. Environment Setup

`# Activate virtual environment
source venv/bin/activate`

`# Install dependencies`
`pip install -r requirements.txt`

2. Running the Application
`python3 run.py`

The API documentation (Swagger) will be available at: `http://localhost:5000/`

3. Running Tests

To verify the system integrity, run:
`export PYTHONPATH=. && python3 -m unittest discover tests`

## 🔍 Implementation Summary

-   **Pattern used**: Facade Pattern for simplified interaction between layers.
    
-   **API Framework**: Flask-RESTx with automatic Swagger documentation.
    
-   **Relationships**: Handled complex data linking (Place-Owner, Place-Review, Place-Amenity).
    
-   **Operations**: Full implementation of CRUD (Create, Read, Update, Delete).
    

----------

**Developed as part of the HBnB Software Engineering curriculum.**

**By David Dufont (github : dufontdd) & Dylan Serigba (github : d-serigba)** 

