from typing import List
from .schemas import MovieCreate, MovieUpdate, Movie

movies = []
next_movie_id = 1

def create_movie(movie: MovieCreate) -> Movie:
    global next_movie_id
    movie_data = movie.dict()
    movie_id = str(next_movie_id)
    next_movie_id += 1
    new_movie = Movie(id=movie_id, **movie_data)
    movies.append(new_movie)
    return new_movie

def get_movie(movie_id: str) -> Movie:
    for movie in movies:
        if movie.id == movie_id:
            return movie
    return None

def get_movies(limit: int = 10, offset: int = 0) -> List[Movie]:
    return movies[offset:offset + limit]

def update_movie(movie_id: str, movie_update: MovieUpdate) -> Movie:
    for movie in movies:
        if movie.id == movie_id:
            update_data = movie_update.dict(exclude_unset=True)
            updated_movie = movie.copy(update=update_data)
            movies.remove(movie)
            movies.append(updated_movie)
            return updated_movie
    return None

def delete_movie(movie_id: str) -> Movie:
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return movie
    return None