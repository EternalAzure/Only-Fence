from flask import Flask
from flask_wtf.csrf import CSRFProtect
from os import getenv
app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

csrf = CSRFProtect()
csrf.init_app(app)

import routes