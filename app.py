from os import getenv
from flask import Flask
from flask import render_template

app = Flask(__name__)
# app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

import routes
