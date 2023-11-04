from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List, Tuple
from .schemas import MovieCreate, MovieUpdate, Movie
from . import crud, config
from .database.database import MongoDB
from uuid import UUID

cfg: config.Config = config.load_config()
MongoDB(mongo_dsn=cfg.mongo_dsn)

app = FastAPI(
    title="Movie Information Service"
)

@app.post("/movies", response_model=Movie)
def create_movie(movie: MovieCreate) -> Movie:
    return crud.create_movie(movie)

@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: UUID) -> Movie:
    movie = crud.get_movie(movie_id)
    if movie is None:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return movie

@app.get("/movies", response_model=Tuple[int, List[Movie]])
def get_movies(limit: int = 10, offset: int = 0) -> Tuple[int, List[Movie]]:
    return crud.get_movies(limit, offset)

@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: UUID, movie_update: MovieUpdate) -> Movie:
    movie = crud.update_movie(movie_id, movie_update)
    if movie is None:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return movie

@app.delete("/movies/{movie_id}", response_model=Movie)
def delete_movie(movie_id: UUID) -> Movie:
    movie = crud.delete_movie(movie_id)
    if movie is None:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return movie