'''Communicates with databe'''


from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from os import getenv
from flask import make_response

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def publish(text: str, image):
    id = _insert_post(text)
    _insert_image(image, id)

def _insert_image(data, posts_id):
    sql = "INSERT INTO images (data, posts_id) VALUES (:data, :posts_id)"
    db.session.execute(sql, {"data":data, "posts_id":posts_id})
    db.session.commit()

def _insert_post(text: str):
    sql = "INSERT INTO posts (text) VALUES (:text) RETURNING id"
    resulting_id = db.session.execute(sql, {"text":text})
    db.session.commit()
    return resulting_id.fetchone()[0]

def select_logo():
    sql = "SELECT data FROM images WHERE r_id=:id" # TODO just example query
    id = 1 # id would be known
    result = db.session.execute(sql, {"id":id})
    try:
        data = result.fetchone()[0]
        response = make_response(bytes(data))
        response.headers.set("Content-Type", "image/jpeg")
        return response
    except TypeError:
        return None