from typing import List, Tuple
from .schemas import MovieCreate, MovieUpdate, Movie
from uuid import UUID

movies = []
next_movie_id = 1

def create_movie(movie: MovieCreate) -> Movie:
    global next_movie_id
    movie_data = movie.dict()
    movie_id = UUID(int=next_movie_id)  # Генерируем UUID из целочисленного значения
    next_movie_id += 1
    new_movie = Movie(id=movie_id, **movie_data)
    movies.append(new_movie)
    return new_movie

def get_movie(movie_id: UUID) -> Movie:
    for movie in movies:
        if movie.id == movie_id:
            return movie
    return None

def get_movies(limit: int = 10, offset: int = 0) -> Tuple[int, List[Movie]]:
    movie_list = movies[offset:offset + limit]
    movies_count = len(movies)
    return movies_count, movie_list

def update_movie(movie_id: UUID, movie_update: MovieUpdate) -> Movie:
    for movie in movies:
        if movie.id == movie_id:
            update_data = movie_update.dict(exclude_unset=True)
            updated_movie = movie.copy(update=update_data)
            movies.remove(movie)
            movies.append(updated_movie)
            return updated_movie
    return None

def delete_movie(movie_id: UUID) -> Movie:
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return movie
    return None