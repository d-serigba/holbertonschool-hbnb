from app.models.user import User
from app.models.base_model import BaseModel

def test_everything():
    print("--- DÉBUT DES TESTS ---")
    
    # 1. Test Base
    base = BaseModel()
    print(f"ID généré : {base.id}")
    
    # 2. Test User
    user = User(first_name="D", last_name="Serigba", email="test@hbnb.com")
    assert user.first_name == "D"
    print("Utilisateur créé avec succès !")
    
    print("--- TOUS LES TESTS SONT VERTS ---")

if __name__ == "__main__":
    test_everything()
