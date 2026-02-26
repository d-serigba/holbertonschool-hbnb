class InMemoryRepository:
    def __init__(self):
        self.data = {
            "users": {},
            "places": {},
            "amenities": {},
            "reviews": {}
        }
        self.counters = {
            "users": 0,
            "places": 0,
            "amenities": 0,
            "reviews": 0
        }

    def add(self, entity_type, obj):
        self.counters[entity_type] += 1
        obj_id = self.counters[entity_type]
        obj["id"] = obj_id
        self.data[entity_type][obj_id] = obj
        return obj

    def get(self, entity_type, obj_id):
        return self.data[entity_type].get(obj_id)

    def get_all(self, entity_type):
        return list(self.data[entity_type].values())

    def update(self, entity_type, obj_id, new_data):
        if obj_id in self.data[entity_type]:
            self.data[entity_type][obj_id].update(new_data)
            return self.data[entity_type][obj_id]
        return None

    def delete(self, entity_type, obj_id):
        return self.data[entity_type].pop(obj_id, None)
