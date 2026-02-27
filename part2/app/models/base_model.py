import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Met à jour la date de modification."""
        self.updated_at = datetime.now()

    def update(self, data):
        """
        Cette méthode est la clé ! 
        Elle permet de mettre à jour les attributs de l'objet.
        """
        for key, value in data.items():
            # On vérifie que l'objet a bien cet attribut (ex: first_name)
            if hasattr(self, key):
                setattr(self, key, value)
        
        # On enregistre la date du changement
        self.save()
