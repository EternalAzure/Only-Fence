from os import getenv
from app import app
from flask_cors import CORS
from flask import render_template, redirect
import db

#Lets client request data from static/index.js through API
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/publish", methods=["POST"])
def publish():
    # TODO
    return redirect("/")

@app.route("/logo", methods=["GET"])
def logo():
    # TODO
    image = db.select_logo()
    if image: return image
    return "No image"