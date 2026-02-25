class InMemoryRepository:
    def __init__(self):
        self.data = {
            "amenities": {},
            "places": {},
            "users": {},
            "reviews": {}
        }

    def add(self, obj_type, obj):
        """Ajoute un objet et lui attribue un id auto-incrémenté"""
        obj_id = len(self.data[obj_type]) + 1
        obj["id"] = obj_id
        self.data[obj_type][obj_id] = obj
        return obj

    def get_all(self, obj_type):
        """Retourne tous les objets d'un type"""
        return list(self.data[obj_type].values())

    def update(self, obj_type, obj_id, new_data):
        """Met à jour un objet existant"""
        if obj_id in self.data[obj_type]:
            self.data[obj_type][obj_id].update(new_data)
            return self.data[obj_type][obj_id]
        return None

    def get_by_id(self, obj_type, obj_id):
        """Retourne un objet par son id"""
        return self.data[obj_type].get(obj_id)
    
    def delete(self, obj_type, obj_id):
        """Supprime un objet par son id"""
        return self.data[obj_type].pop(obj_id, None)
