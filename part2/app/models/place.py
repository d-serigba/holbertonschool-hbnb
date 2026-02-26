from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        
        # --- PHASE DE VALIDATION (Le "Vigile") ---
        if not title:
            raise ValueError("Le titre est obligatoire.")
        
        if price < 0:
            raise ValueError("Le prix doit être un nombre positif.")
            
        if not (-90 <= latitude <= 90):
            raise ValueError("La latitude doit être comprise entre -90 et 90.")
            
        if not (-180 <= longitude <= 180):
            raise ValueError("La longitude doit être comprise entre -180 et 180.")
            
        if owner is None:
            raise ValueError("Un logement doit avoir un propriétaire (owner).")

        # --- PHASE D'ASSIGNATION ---
        self.title = title
        self.description = description
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = owner  # Objet User
        self.amenities = [] # Liste d'objets Amenity
        self.reviews = []   # Liste d'objets Review

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
