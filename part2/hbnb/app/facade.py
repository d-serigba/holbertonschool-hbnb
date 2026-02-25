from app.models.persistence.in_memory_repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.repo = InMemoryRepository()

    # ----------------- AMENITIES -----------------
    def create_amenity(self, data):
        return self.repo.add("amenities", data)

    def get_amenities(self):
        return self.repo.get_all("amenities")

    def update_amenity(self, obj_id, data):
        return self.repo.update("amenities", obj_id, data)

    def delete_amenity(self, obj_id):
        return self.repo.delete("amenities", obj_id)

    # ----------------- PLACES -----------------
    def create_place(self, data):
        return self.repo.add("places", data)

    def get_places(self):
        return self.repo.get_all("places")

    def update_place(self, obj_id, data):
        return self.repo.update("places", obj_id, data)

    def delete_place(self, obj_id):
        return self.repo.delete("places", obj_id)

    # ----------------- USERS -----------------
    def create_user(self, data):
        return self.repo.add("users", data)

    def get_users(self):
        return self.repo.get_all("users")

    def update_user(self, obj_id, data):
        return self.repo.update("users", obj_id, data)

    def delete_user(self, obj_id):
        return self.repo.delete("users", obj_id)

    # ----------------- REVIEWS -----------------
    def create_review(self, data):
        return self.repo.add("reviews", data)

    def get_reviews(self):
        return self.repo.get_all("reviews")

    def update_review(self, obj_id, data):
        return self.repo.update("reviews", obj_id, data)

    def delete_review(self, obj_id):
        return self.repo.delete("reviews", obj_id)
