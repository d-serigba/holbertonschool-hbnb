import unittest
import json
from app import create_app

class TestHBnBAPI(unittest.TestCase):
    def setUp(self):
        """Configuration avant chaque test : on lance l'app en mode test."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user_success(self):
        """Test : Création d'un utilisateur valide (Succès attendu)"""
        response = self.client.post('/api/v1/users/', 
            data=json.dumps({
                "first_name": "D", 
                "last_name": "Serigba", 
                "email": "ceo@glassier.com"
            }),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_review_invalid_rating(self):
        """Test : Création d'une review avec note de 10/5 (Échec attendu)"""
        # On tente de poster une note interdite
        response = self.client.post('/api/v1/reviews/', 
            data=json.dumps({
                "text": "Pas mal",
                "rating": 10,  # <--- ERREUR VOLONTAIRE
                "user_id": "fake-id",
                "place_id": "fake-id"
            }),
            content_type='application/json')
        
        # Le système doit répondre 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
