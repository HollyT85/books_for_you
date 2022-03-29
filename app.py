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
    """allow a new user to register and save into DB"""
    if request.method == "POST":
        existing_username = mongo.db.find_one(
            {"username": request.form.get("username").lower})

        if existing_username():
            flash("Username taken")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session['user'] = request.form.get("username").lower()
        flash("Account succesfully created")
        return redirect(url_for("userprofile", username=session["user"]))

    return render_template("register.html")


# log in function
@app.route("/login", methods=["GET", "POST"])
def login():
    """check if username exists"""
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password matches with username and display an error
            # if it doesn't
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))

                return redirect(url_for(
                    "userprofile", username=session["user"]))
        else:
            flash("Incorrect username or password. Please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
