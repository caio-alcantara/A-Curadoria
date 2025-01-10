# backend/app/create_app.py
from flask import Flask
import os
from flask_cors import CORS  # Importa o CORS

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "default_secret_key")
    CORS(app)
    
    # Importa as rotas
    from app.routes.movies_routes import movie_bp  # Importa as rotas de filmes
    app.register_blueprint(movie_bp, url_prefix='/api')  # Registra o blueprint com prefixo '/api'

    return app
