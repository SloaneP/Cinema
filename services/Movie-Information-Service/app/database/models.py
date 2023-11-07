from mongoengine import Document, StringField, IntField, ListField, UUIDField
from uuid import uuid4
from bson import ObjectId

class Movie(Document):
    id = UUIDField(primary_key=True, default=uuid4, binary=False)
    title = StringField(required=True)
    description = StringField(required=True)
    genre = StringField(required=True)
    actors = ListField(StringField(), required=True)
    release_year = IntField(required=True)

    def __str__(self):
        return f"Movie(_id={str(self.id)}, title={self.title}, description={self.description}, genre={self.genre}, actors={self.actors}, release_year={self.release_year})"