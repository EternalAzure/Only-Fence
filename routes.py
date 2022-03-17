from os import getenv
from app import app
from flask_cors import CORS
from flask import render_template, redirect, request
import db

#Lets client request data from static/index.js through API
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def index():
    print("INFO: /index")
    posts = db.get_posts()
    return render_template("index.html", posts=posts)

@app.route("/publish", methods=["POST"])
def publish():
    print("INFO: /publish")
    text = request.form["text"]
    image = request.files["file"]
    db.publish(text, image)
    print("INFO: past publishing")
    return redirect("/")

@app.route("/image/<int:id>")
def image(id):
    return db.get_image(id)

@app.route("/delete/<int:id>")
def delete(id):
    db.delete_post(id)
    return redirect("/")