from flask import Blueprint, jsonify, request
import requests
import os
from app.models import Movie
from app.services import find_movie_id_by_name, get_movie_recommendations_by_id

movie_bp = Blueprint('movie_bp', __name__)

API_KEY = os.getenv("API_KEY")

# Função para obter detalhes de um filme
@movie_bp.route('/movie/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en"
    response = requests.get(url)
    return jsonify(response.json())

# Função para buscar filmes por nome
@movie_bp.route('/search', methods=['GET'])
def search_movies():
    query = request.args.get('query')  # Obtém o parâmetro 'query' da URL
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}&language=en"
    response = requests.get(url)
    return jsonify(response.json())

# Função para obter filmes populares
@movie_bp.route('/popular', methods=['GET'])
def get_popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en"
    response = requests.get(url)
    return jsonify(response.json())

# Função para obter filmes por gênero
@movie_bp.route('/genre/<int:genre_id>', methods=['GET'])
def get_movies_by_genre(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en"
    response = requests.get(url)
    return jsonify(response.json())

# Função para obter recomendações a partir de um filme
@movie_bp.route('<int:movie_id>/recommendations', methods=['GET'])
def get_recommendations(movie_id):
    recommendations = get_movie_recommendations_by_id(movie_id)
    return jsonify(recommendations)

@movie_bp.route('find_id/<string:movie_name>', methods=['GET'])
def get_movie_id_by_name(movie_name):
    if not movie_name:
        return jsonify({'error': 'No movie name provided'})
    
    movie_id = find_movie_id_by_name(movie_name)
    if not movie_id:
        return jsonify({'error': 'Movie not found'}), 404
    
    return jsonify({'movie_id': movie_id})
