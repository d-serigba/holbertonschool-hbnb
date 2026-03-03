<<<<<<< HEAD
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
=======
---

## Résumé HTTP vs HTTPS

**HTTP (HyperText Transfer Protocol)**

* Protocole utilisé pour communiquer entre navigateur et serveur.
* Les données circulent en clair (non chiffrées).
* Risque : interception ou modification des données.

**HTTPS (HTTP Secure)**

* Version sécurisée de HTTP.
* Utilise un chiffrement (SSL/TLS).
* Protège les données contre interception et piratage.
* Aujourd’hui utilisé sur la majorité des sites.

Différence principale : HTTPS = sécurisé, HTTP = non sécurisé.

---

## Structure d’une requête et réponse HTTP

### Requête HTTP (envoyée par le client)

Elle contient :

* Méthode → action (GET, POST…).
* URL / chemin → ressource demandée.
* Headers (en-têtes) → infos supplémentaires
  (type de données, authentification…).
* Body (optionnel) → données envoyées
  (ex : formulaire, JSON).

Exemple simple :

```
GET /users HTTP/1.1
Host: example.com
Authorization: token
```

---

### Réponse HTTP (envoyée par le serveur)

Elle contient :

* Code statut → résultat (200, 404…).
* Headers → type de contenu, taille…
* Body → données retournées
  (souvent JSON ou HTML).

Exemple :

```
HTTP/1.1 200 OK
Content-Type: application/json
```

Puis les données JSON.

---

## Méthodes HTTP + cas d’usage

### GET

* Sert à récupérer des données.
* Exemple : afficher une page ou récupérer infos API.

### POST

* Sert à envoyer ou créer des données.
* Exemple : formulaire d’inscription.

### PUT / PATCH

* 
# HBnB – Part 2: REST API

## Description

Cette partie du projet HBnB implémente une API REST structurée en couches avec :

-   Modèles métier
    
-   Services (logique métier)
    
-   Facade (centralisation des appels)
    
-   Repository (persistence)
    
-   Endpoints HTTP testés
    

L’objectif est d’appliquer une architecture claire, maintenable et évolutive.

----------

## Architecture

L’application suit une architecture en couches :

Client → Routes → Services → Facade → Repository → Models

-   Models : définissent les entités (User, Place, Review, Amenity).
    
-   Services : contiennent la logique métier et les validations.
    
-   Facade : simplifie l’accès aux services.
    
-   Repository : gère le stockage des objets.
    
-   Routes : exposent les endpoints REST.
>>>>>>> ce40a0c99af2487d6cc20d2f0220cf0c9793ef37
    

----------

<<<<<<< HEAD
**Developed as part of the HBnB Software Engineering curriculum.**

**By David Dufont (github : dufontdd) & Dylan Serigba (github : d-serigba)** 

=======
## Lancement

Depuis le dossier `hbnb` :

pip install -r requirements.txt  
python3 run.py

Le serveur démarre sur `http://127.0.0.1:5000`.

----------

## Codes de retour HTTP

Les endpoints respectent les codes suivants :

-   201 Created : ressource créée avec succès.
    
-   200 OK : requête traitée avec succès.
    
-   400 Bad Request : erreur de validation (données invalides).
    
-   404 Not Found : ressource inexistante.
    

----------

## Problème rencontré

Une erreur d’indentation dans `facade.py` empêchait le serveur de démarrer :

IndentationError: expected an indented block after function definition

Après correction de l’indentation :

-   Le serveur démarre correctement.
    
-   Tous les endpoints retournent les codes attendus.
    
-   Les tests de la Task 6 sont validés.
    

----------

## Conclusion

Cette partie met en œuvre :

-   Une séparation claire des responsabilités
    
-   Une gestion correcte des erreurs HTTP
    
-   Une API REST fonctionnelle et testéeq

---
>>>>>>> ce40a0c99af2487d6cc20d2f0220cf0c9793ef37
