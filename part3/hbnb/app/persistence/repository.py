# app/persistence/repository.py

from app.models.base_model import db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class SQLAlchemyRepository:
    """Repository générique utilisant SQLAlchemy pour CRUD."""

    def __init__(self, session):
        self.session = session

    # ---------------- Add ----------------
    def add(self, obj):
        self.session.add(obj)
        self.session.commit()
        return obj

    # ---------------- Update ----------------
    def update(self, obj):
        self.session.commit()
        return obj

    # ---------------- Delete ----------------
    def delete(self, obj):
        self.session.delete(obj)
        self.session.commit()
        return True

    # ---------------- Get by ID ----------------
    def get(self, model_class, obj_id):
        return self.session.query(model_class).get(obj_id)

    # ---------------- Get all ----------------
    def get_all(self, model_class):
        return self.session.query(model_class).all()

    # ---------------- User-specific ----------------
    def get_by_email(self, model_class, email):
        return self.session.query(model_class).filter_by(email=email).first()

    # ---------------- Review convenience ----------------
    def get_review_by_user_and_place(self, user_id, place_id):
        return self.session.query(Review).filter_by(user_id=user_id, place_id=place_id).first()
