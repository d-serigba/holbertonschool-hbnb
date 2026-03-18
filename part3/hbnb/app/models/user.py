# app/models/user.py

from .base_model import BaseModel, db
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from flask_bcrypt import generate_password_hash, check_password_hash

class User(BaseModel):
    __tablename__ = "users"

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    _password = Column("password", String(128), nullable=False)
    is_admin = Column(Boolean, default=False)

    # Relationships
    places = relationship("Place", back_populates="owner", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")

    # ---------------- Password ----------------
    @property
    def password(self):
        return None

    @password.setter
    def password(self, plain_password):
        self._password = generate_password_hash(plain_password).decode("utf-8")

    def check_password(self, plain_password):
        return check_password_hash(self._password, plain_password)

    # ---------------- to_dict ----------------
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
