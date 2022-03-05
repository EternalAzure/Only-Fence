from os import getenv
from app import app
from flask_cors import CORS
from flask import render_template

#Lets client request data from static/index.js through API
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def index():
    return render_template("index.html")