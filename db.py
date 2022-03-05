'''Communicates with databe'''


from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from os import getenv
from flask import make_response

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def insert_post(a, b, c):
    # TODO
    sql = "INSERT INTO posts (a, b, c) VALUES (:a, :b, :c)"
    db.session.execute(sql, {"a":a, "b":b, "c":c})
    db.session.commit()
    pass

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