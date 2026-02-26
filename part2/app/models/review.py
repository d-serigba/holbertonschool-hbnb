from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        # Validations de base
        if not text:
            raise ValueError("Le texte de l'avis ne peut pas être vide.")
        if not (1 <= rating <= 5):
            raise ValueError("La note doit être comprise entre 1 et 5.")
        
        self.text = text
        self.rating = rating
        self.place = place  # Objet Place concerné
        self.user = user    # Objet User (l'auteur)
