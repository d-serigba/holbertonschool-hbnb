from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place  # <--- Assure-toi que cet import est présent

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # --- LOGIQUE UTILISATEURS ---
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        return self.user_repo.update(user_id, user_data)

    # --- LOGIQUE AMENITIES ---
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)

    # --- LOGIQUE PLACES (Tâche 4) ---
    def create_place(self, place_data):
        # On extrait l'ID (le texte)
        owner_id = place_data.pop('owner_id', None)
        # On va chercher le vrai pilote (l'objet User)
        owner = self.get_user(owner_id)
        
        if not owner:
            return None

        # On installe le vrai pilote dans les données de la Place
        place_data['owner'] = owner
        
        # On lance la fabrication
        new_place = Place(**place_data)
        self.place_repo.add(new_place)
        return new_place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        return self.place_repo.update(place_id, place_data)
        
    def add_amenity_to_place(self, place_id, amenity_id):
        """Lien entre un logement et un équipement."""
        place = self.get_place(place_id)
        amenity = self.get_amenity(amenity_id)
        
        if place and amenity:
            # On utilise la méthode add_amenity que tu as créée dans ton modèle Place
            place.add_amenity(amenity)
            return place
        return None
