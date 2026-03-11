from sqlalchemy import Column, String, Float, ForeignKey
from .base_model import BaseModel

class Place(BaseModel):
    __tablename__ = 'places'

    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    owner_id = Column(String(60), ForeignKey('users.id'), nullable=False)  # <-- ajout ici

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id
        }
