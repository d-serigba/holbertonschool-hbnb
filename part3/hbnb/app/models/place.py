# app/models/place.py

from .base_model import BaseModel, db
from sqlalchemy import Column, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

# Association table for many-to-many Place <-> Amenity
place_amenity = Table(
    "place_amenity",
    db.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True)
)

class Place(BaseModel):
    __tablename__ = "places"

    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    owner_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    # Relationships
    owner = relationship("User", back_populates="places")
    reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        back_populates="places"
    )

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
