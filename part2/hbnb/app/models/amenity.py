# app/models/amenity.py
from .base_model import BaseModel
from sqlalchemy import Column, String

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    description = Column(String(256))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
