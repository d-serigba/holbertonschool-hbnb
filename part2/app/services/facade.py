from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        # On initialise les 4 réservoirs de données
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # --- LOGIQUE POUR LES UTILISATEURS ---

    def create_user(self, user_data):
        """Crée un utilisateur, l'enregistre et le renvoie."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Récupère un utilisateur par son ID."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Récupère un utilisateur par son email (utile pour la validation)."""
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """Récupère la liste complète des utilisateurs."""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """Met à jour les informations d'un utilisateur."""
        return self.user_repo.update(user_id, user_data)

    # --- PLACEHOLDERS POUR LA SUITE ---
    # Ces méthodes seront implémentées dans les tâches suivantes
    def get_place(self, place_id):
        pass
