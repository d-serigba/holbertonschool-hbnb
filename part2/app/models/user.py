from .base_model import BaseModel  # Plus robuste pour les tests

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()  # On initialise l'ID et les dates du BaseModel
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        
        # Validation : L'exigence Glassier
        if not self.email:
            raise ValueError("L'email est obligatoire")
