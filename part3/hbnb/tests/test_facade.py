from app.facade import HBnBFacade

def main():
    facade = HBnBFacade()

    # Test création d'un utilisateur
    user = {"email": "test@example.com", "password": "1234", "first_name": "Test", "last_name": "User"}
    created_user = facade.create_user(user)
    print("Utilisateur créé :", created_user)

    # Test création d'une place
    place = {"title": "Appartement cosy", "description": "Petit appartement charmant", "price": 50.0, "latitude": 48.8566, "longitude": 2.3522}
    created_place = facade.create_place(place)
    print("Place créée :", created_place)

    # Test création d'une amenity
    amenity = {"name": "Piscine", "description": "Piscine chauffée"}
    created_amenity = facade.create_amenity(amenity)
    print("Amenity créée :", created_amenity)

    # Vérification récupération des listes
    print("Tous les utilisateurs :", facade.get_users())
    print("Toutes les places :", facade.get_places())
    print("Toutes les amenities :", facade.get_amenities())

if __name__ == "__main__":
    main()
