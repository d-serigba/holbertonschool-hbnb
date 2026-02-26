from app.models.place import Place
from app.models.user import User

def test_place_logic():
    print("--- DÉBUT DES TESTS DE VALIDATION (PLACE) ---")
    
    # On crée un propriétaire valide pour le test
    owner = User(first_name="Alice", last_name="Doe", email="alice@test.com")

    # 1. TEST : Données valides
    try:
        p1 = Place(title="Vila", description="Belle vue", price=150.0, 
                   latitude=48.8566, longitude=2.3522, owner=owner)
        print("✅ Succès : Logement valide créé.")
    except Exception as e:
        print(f"❌ Échec : Le logement valide a été rejeté. Erreur : {e}")

    # 2. TEST : Prix négatif (Doit échouer)
    try:
        p2 = Place(title="Gratuit", description="Pas cher", price=-10, 
                   latitude=48.8, longitude=2.3, owner=owner)
        print("❌ Échec : Le système a accepté un prix négatif !")
    except ValueError as e:
        print(f"✅ Succès : Prix négatif rejeté comme prévu. (Erreur : {e})")

    # 3. TEST : Latitude invalide (Doit échouer)
    try:
        p3 = Place(title="Mars", description="Trop loin", price=100, 
                   latitude=120.0, longitude=2.3, owner=owner)
        print("❌ Échec : Le système a accepté une latitude de 120 !")
    except ValueError as e:
        print(f"✅ Succès : Latitude invalide rejetée. (Erreur : {e})")

    print("--- FIN DES TESTS ---")

if __name__ == "__main__":
    test_place_logic()
