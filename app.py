"""
Imports for functionality
"""
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

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
    """return user to home page"""
    return render_template("home.html")


# register function
@app.route("/register", methods=["GET", "POST"])
def register():
    """ action to take if method is post """
    if request.method == "POST":
        # Check if username exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # tell user if username already exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # save to mongo
        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registration)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("login"))

    return render_template("register.html")


# log in function
@app.route("/login", methods=["GET", "POST"])
def login():
    # if method is post
    if request.method == "POST":
        # Check if username exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password matches users input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # username / password incorrect
                flash("Username/Password incorrect. Please try again.")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Username/Password incorrect. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
