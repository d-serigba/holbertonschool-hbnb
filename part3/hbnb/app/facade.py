# facade.py
from .models.base_model import db
from .models.user import User
from .models.place import Place
from .models.amenity import Amenity
from .models.review import Review


class HBnBFacade:

    # ---------------- USERS ----------------
    def create_user(self, data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user  # retourne l'objet, pas dict

    def get_users(self):
        return User.query.all()  # liste d'objets

    def get_user(self, user_id):
        return User.query.get(user_id)  # objet ou None

    def update_user(self, obj_id, data):
        user = User.query.get(obj_id)
        if not user:
            return None

        for key, value in data.items():
            setattr(user, key, value)

        db.session.commit()
        return user  # objet

    def delete_user(self, obj_id):
        user = User.query.get(obj_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True


    # ---------------- PLACES ----------------
    def create_place(self, data):
        required_fields = ["title", "price", "owner_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} is required")

        if not isinstance(data.get("price"), (int, float)):
            raise ValueError("price must be a number")

        if "latitude" in data and data["latitude"] is not None and not isinstance(data["latitude"], (int, float)):
            raise ValueError("latitude must be a number")

        if "longitude" in data and data["longitude"] is not None and not isinstance(data["longitude"], (int, float)):
            raise ValueError("longitude must be a number")

        owner = User.query.get(data["owner_id"])
        if not owner:
            raise ValueError("owner_id does not correspond to any user")

        place = Place(**data)
        db.session.add(place)
        db.session.commit()
        return place  # objet

    def get_places(self):
        return Place.query.all()

    def get_place(self, place_id):
        return Place.query.get(place_id)

    def update_place(self, obj_id, data):
        place = Place.query.get(obj_id)
        if not place:
            return None

        if "price" in data and not isinstance(data["price"], (int, float)):
            raise ValueError("price must be a number")

        if "latitude" in data and data["latitude"] is not None and not isinstance(data["latitude"], (int, float)):
            raise ValueError("latitude must be a number")

        if "longitude" in data and data["longitude"] is not None and not isinstance(data["longitude"], (int, float)):
            raise ValueError("longitude must be a number")

        if "owner_id" in data:
            owner = User.query.get(data["owner_id"])
            if not owner:
                raise ValueError("owner_id does not correspond to any user")

        for key, value in data.items():
            setattr(place, key, value)

        db.session.commit()
        return place  # objet

    def delete_place(self, obj_id):
        place = Place.query.get(obj_id)
        if not place:
            return False

        db.session.delete(place)
        db.session.commit()
        return True


    # ---------------- AMENITIES ----------------
    def create_amenity(self, data):
        amenity = Amenity(**data)
        db.session.add(amenity)
        db.session.commit()
        return amenity  # objet

    def get_amenities(self):
        return Amenity.query.all()

    def update_amenity(self, obj_id, data):
        amenity = Amenity.query.get(obj_id)
        if not amenity:
            return None

        for key, value in data.items():
            setattr(amenity, key, value)

        db.session.commit()
        return amenity  # objet

    def delete_amenity(self, obj_id):
        amenity = Amenity.query.get(obj_id)
        if not amenity:
            return False

        db.session.delete(amenity)
        db.session.commit()
        return True


    # ---------------- REVIEWS ----------------
    def create_review(self, data):
        review = Review(**data)
        db.session.add(review)
        db.session.commit()
        return review  # objet

    def get_reviews(self):
        return Review.query.all()

    def get_review(self, obj_id):
        return Review.query.get(obj_id)

    def update_review(self, obj_id, data):
        review = Review.query.get(obj_id)
        if not review:
            return None

        for key, value in data.items():
            setattr(review, key, value)

        db.session.commit()
        return review  # objet

    def delete_review(self, obj_id):
        review = Review.query.get(obj_id)
        if not review:
            return False

        db.session.delete(review)
        db.session.commit()
        return True
