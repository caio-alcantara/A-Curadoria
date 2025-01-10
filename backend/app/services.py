import requests
import os

api_key = os.getenv("API_KEY")

def get_movie_recommendations_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    recommendations = []
    for movie in data.get('results', [])[:5]:  # Pegue apenas os primeiros 5 filmes
        recommendations.append({
            'title': movie['title'],
            'genre': ', '.join([genre['name'] for genre in movie.get('genres', [])]),
            'year': movie['release_date'].split('-')[0],  
            'overview': movie['overview'],
            'poster': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else None
        })
    
    return recommendations
    
def find_movie_id_by_name(movie_name):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': movie_name,
        'language': 'en-US',
        'page': 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Verifica se o retorno contém resultados
    if data.get('results'):
        # Retorna o ID do primeiro filme encontrado
        movie_id = data['results'][0]['id']
        return movie_id
    else:
        # Caso não encontre o filme
        return None
