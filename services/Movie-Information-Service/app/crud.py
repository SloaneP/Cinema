from typing import List, Tuple, Optional
from .schemas import MovieCreate, MovieUpdate, Movie
from app.database.models import Movie as MovieModel
from uuid import UUID

def create_movie(movie: MovieCreate) -> Movie:
    movie_data = movie.dict()
    new_movie = MovieModel(**movie_data)
    new_movie.save()
    return new_movie

def get_movie(movie_id: UUID) -> Optional[Movie]:
    movie = MovieModel.objects(id=movie_id).first()
    return movie

def get_movies(limit: int = 10, offset: int = 0) -> Tuple[int, List[Movie]]:
    movies = MovieModel.objects.skip(offset).limit(limit)
    movies_count = MovieModel.objects.count()
    return movies_count, list(movies)

def update_movie(movie_id: UUID, movie_update: MovieUpdate) -> Optional[Movie]:
    movie = MovieModel.objects(id=movie_id).first()
    if movie:
        update_data = movie_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(movie, field, value)
        movie.save()
        return movie
    return None

def delete_movie(movie_id: UUID) -> Optional[Movie]:
    movie = MovieModel.objects(id=movie_id).first()
    if movie:
        movie.delete()
        return movie
    return None