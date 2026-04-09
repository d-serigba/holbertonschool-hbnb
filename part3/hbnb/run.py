# run.py
from app import create_app
from flask_cors import CORS

app = create_app()

# Configuration CORS étendue pour supporter POST et Authorization headers
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Origin"]
    }
})

if __name__ == "__main__":
    # debug=True pour rechargement automatique et affichage des erreurs
    app.run(debug=True)
