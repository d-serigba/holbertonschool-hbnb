from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        # On valide que le nom n'est pas vide
        if not name:
            raise ValueError("L'équipement doit avoir un nom.")
        self.name = name
