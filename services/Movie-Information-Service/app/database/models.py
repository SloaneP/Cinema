from mongoengine import Document, StringField, IntField, ListField

class Movie(Document):
    title = StringField(required=True)
    description = StringField()
    genre = StringField()
    actors = ListField(StringField())
    release_year = IntField()

    def __str__(self):
        return f"Movie(title={self.title}, description={self.description}, genre={self.genre}, actors={self.actors}, release_year={self.release_year})"
