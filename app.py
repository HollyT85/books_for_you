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
from flask_avatars import Avatars
from flask_gravatar import Gravatar


# check for env.py file
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
avatars = Avatars(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# set configurations
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
UPLOAD_FOLDER = "/workspace/books_for_you/static/images/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["ALLOWED_EXTENSIONS"] = ALLOWED_EXTENSIONS

mongo = PyMongo(app)


# home page function
@app.route("/")
def home_page():
    """return user to home page"""
    return render_template("index.html")


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
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registration)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("userprofile", username=session["user"]))

    return render_template("register.html")


# log in function
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    if method is post check if username exists in Mongo
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password matches, if it does, log in
            if check_password_hash(existing_user["password"],
                request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "userprofile", username=session["user"]))

            else:
                # username / password incorrect
                flash("Username/Password incorrect. Please try again.")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Username/Password incorrect. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/userprofile/<username>", methods=["GET", "POST"])
def userprofile(username):
    """
    get users username from db to load userprofile
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    reviews = mongo.db.reviews.find()

    if session["user"]:
        return render_template(
            "userprofile.html", username=username, reviews=list(reviews))

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    advise user they are logged out
    """
    flash("You have been logged out")
    session.pop("user")
    return render_template("index.html")


@app.route("/addbook", methods=["GET", "POST"])
def addbook():
    """
    Add a book to the database
    """
    if request.method == "POST":
        book = {
            "image": request.form.get("image"),
            "title": request.form.get("title").title(),
            "author": request.form.get("author").title(),
            "genre": request.form.get("genre").title(),
        }
        mongo.db.books.insert_one(book)
        flash("Book successfully added. Thanks!")
        return redirect(url_for("browsebooks"))

    return render_template("addbook.html")


@app.route("/addreview", methods=["GET", "POST"])
def addreview():
    """
    Allow user to leave a review
    """
    if request.method == "POST":

        review = {
            "title": request.form.get("title").title(),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "review_by": session["user"].title()
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added. Thanks!")
        return redirect(url_for("browsebooks"))

    return render_template("addreview.html")


@app.route("/books")
def browsebooks():
    """
    Allow user to view books on system
    """
    books = mongo.db.books.find()
    reviews = mongo.db.reviews.find()
    return render_template("books.html", books=books, reviews=list(reviews))


# custom error pages
@app.errorhandler(404)
def page_not_found(e):
    """
    incorrect page custom page
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(err):
    """
    server error custom page
    """
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
