from typing import List
from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str
    genre: str
    actors: List[str]
    release_year: int


class MovieCreate(MovieBase):
    #id: UUID4
    pass


class MovieUpdate(MovieBase):
    pass

class Movie(MovieBase):
    id: str
