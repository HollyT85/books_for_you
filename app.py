"""
Imports for functionality
"""
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# check for env.py file
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# set configurations
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# home page function
@app.route("/")
def home_page():
    return render_template("home.html")


# log in function
@app.route("/login", methods={"GET", "POST"})
def login():
    return render_template("login.html")


# register function
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
