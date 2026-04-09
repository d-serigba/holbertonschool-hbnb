# app/facade.py

from app.models.base_model import db
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository


class HBnBFacade:
    """Façade pour gérer les opérations CRUD sur Users, Places, Amenities et Reviews"""

    def __init__(self):
        # Repository SQLAlchemy avec la session de la base
        self.repo = SQLAlchemyRepository(db.session)

    # ---------------- USERS ----------------
    def create_user(self, data):
        user = User(**data)
        return self.repo.add(user)

    def get_users(self):
        return self.repo.get_all(User)

    def get_user(self, user_id):
        return self.repo.get(User, user_id)

    def get_user_by_email(self, email):
        return self.repo.get_by_email(User, email)

    def update_user(self, obj_id, data):
        user = self.get_user(obj_id)
        if not user:
            return None
        for key, value in data.items():
            setattr(user, key, value)
        return self.repo.update(user)

    def delete_user(self, obj_id):
        user = self.get_user(obj_id)
        if not user:
            return False
        self.repo.delete(user)
        return True

    # ---------------- PLACES ----------------
    def create_place(self, data):
        required_fields = ["title", "price", "owner_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} is required")
        owner = self.get_user(data["owner_id"])
        if not owner:
            raise ValueError("owner_id does not correspond to any user")
        place = Place(**data)
        return self.repo.add(place)

    def get_places(self):
        return self.repo.get_all(Place)

    def get_place(self, place_id):
        return self.repo.get(Place, place_id)

    def update_place(self, obj_id, data):
        place = self.get_place(obj_id)
        if not place:
            return None
        for key, value in data.items():
            setattr(place, key, value)
        return self.repo.update(place)

    def delete_place(self, obj_id):
        place = self.get_place(obj_id)
        if not place:
            return False
        self.repo.delete(place)
        return True

    # ---------------- AMENITIES ----------------
    def create_amenity(self, data):
        amenity = Amenity(**data)
        return self.repo.add(amenity)

    def get_amenities(self):
        return self.repo.get_all(Amenity)

    def update_amenity(self, obj_id, data):
        amenity = self.repo.get(Amenity, obj_id)
        if not amenity:
            return None
        for key, value in data.items():
            setattr(amenity, key, value)
        return self.repo.update(amenity)

    def delete_amenity(self, obj_id):
        amenity = self.repo.get(Amenity, obj_id)
        if not amenity:
            return False
        self.repo.delete(amenity)
        return True

    # ---------------- REVIEWS ----------------
    def create_review(self, data):
        review = Review(**data)
        return self.repo.add(review)

    def get_reviews(self):
        return self.repo.get_all(Review)

    def get_review(self, obj_id):
        return self.repo.get(Review, obj_id)

    def update_review(self, obj_id, data):
        review = self.repo.get(Review, obj_id)
        if not review:
            return None
        for key, value in data.items():
            setattr(review, key, value)
        return self.repo.update(review)

    def delete_review(self, obj_id):
        review = self.repo.get(Review, obj_id)
        if not review:
            return False
        self.repo.delete(review)
        return True

    # ---------------- Review convenience ----------------
    def get_review_by_user_and_place(self, user_id, place_id):
        return self.repo.get_review_by_user_and_place(user_id, place_id)
