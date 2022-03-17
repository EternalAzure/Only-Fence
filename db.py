'''Communicates with databe'''


from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask import make_response

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("HEROKU_POSTGRESQL_AQUA_URL")
db = SQLAlchemy(app)

def publish(text: str, image):
    id = _insert_post(text)
    name: str = image.filename
    jpg = name.endswith(".jpg")
    jpeg = name.endswith(".jpeg")
    if not jpg and not jpeg:
        return
    _insert_image(image.read(), id)

def _insert_image(data, posts_id):
    if not data: return
    sql = "INSERT INTO images (data, posts_id) VALUES (:data, :posts_id)"
    db.session.execute(sql, {"data":data, "posts_id":posts_id})
    db.session.commit()

def _insert_post(text: str):
    sql = "INSERT INTO posts (text) VALUES (:text) RETURNING id"
    resulting_id = db.session.execute(sql, {"text":text})
    db.session.commit()
    return resulting_id.fetchone()[0]

def get_posts():
    print("INFO: get_posts()")
    sql = "SELECT posts.id as id, text, data FROM posts LEFT JOIN images ON posts.id = posts_id"
    result = db.session.execute(sql)
    data = result.fetchall()
    posts = []
    for d in data:
        img = False
        if d.data:
            img = True
        posts.append({
            "id": d.id,
            "text": d.text,
            "image": img
        })
    return posts

def get_image(id):
    sql = "SELECT data FROM images WHERE posts_id=:id"
    result = db.session.execute(sql, {"id":id})
    try:
        data = result.fetchone()[0]
        response = make_response(bytes(data))
        response.headers.set("Content-Type", "image/jpeg")
        return response
    except TypeError:
        return None

def delete_post(id: int):
    sql = "DELETE FROM posts WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
