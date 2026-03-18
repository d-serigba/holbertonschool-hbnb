# app/models/review.py

from sqlalchemy import Column, String, ForeignKey
from .base_model import BaseModel
from sqlalchemy.orm import relationship

class Review(BaseModel):
    __tablename__ = "reviews"

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    text = Column(String(512), nullable=False)

    # Relationships
    user = relationship("User", back_populates="reviews")
    place = relationship("Place", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "place_id": self.place_id,
            "text": self.text,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
