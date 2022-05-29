<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
#from .Comment import Comment, CommentSchema
import datetime
# title, isbn, author, year, image src, read
class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(360))
    author = db.Column(db.String(360))
    year = db.Column(db.Integer, nullable = True)
    image_source = db.Column(db.String(360))
    read = db.Column(db.Boolean)
=======
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
#from .Comment import Comment, CommentSchema
import datetime
# title, isbn, author, year, image src, read
class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(360))
    author = db.Column(db.String(360))
    year = db.Column(db.Integer, nullable = True)
    image_source = db.Column(db.String(360))
    read = db.Column(db.Boolean)
>>>>>>> 88673f121d75e9b1ec329028737e20ff6be35a53
