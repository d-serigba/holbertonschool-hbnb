# tests/test_facade_app.py
from app import create_app

def test_facade():
    app = create_app()
    facade = app.facade

    # Création d'un utilisateur via le facade
    user = facade.create_user({
        "email": "test@app.com",
        "password": "1234",
        "first_name": "Test",
        "last_name": "User"
    })
    print("Utilisateur créé :", user)

    # Création d'une place
    place = facade.create_place({
        "title": "Studio sympa",
        "description": "Petit studio agréable",
        "price": 40.0,
        "latitude": 48.85,
        "longitude": 2.35
    })
    print("Place créée :", place)

    # Récupération de tous les utilisateurs
    all_users = facade.get_users()
    print("Tous les utilisateurs :", all_users)

if __name__ == "__main__":
    test_facade()
