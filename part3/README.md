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
    

----------

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
