import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        # Génère un identifiant unique universel (ex: 550e8400-e29b...)
        self.id = str(uuid.uuid4())
        # Enregistre l'heure précise de création
        self.created_at = datetime.now()
        # Initialise l'heure de modification
        self.updated_at = datetime.now()

    def save(self):
        """Met à jour la date de modification."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Prépare les données pour être envoyées en format JSON."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
