"""
Imports for functionality
"""
import os
import datetime
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
        # check passwords match
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if password1 != password2:
            flash("Passwords do not match. Please try again.")
            return redirect(url_for("register"))
        # save to mongo
        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password1"))
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
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(
                    url_for("userprofile", username=session["user"]))

            else:
                # username / password incorrect
                flash("Username/Password incorrect. Please try again.")
                return redirect(url_for("login"))

        else:
            # username / password incorrect
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

    # let user go to profile page
    if session["user"]:
        return render_template(
            "userprofile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    advise user they are logged out
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home_page"))


@app.route("/addbook", methods=["GET", "POST"])
def addbook():
    """
    Add a book to the database
    """

    # so books can be displayed by most recent
    today = datetime.datetime.now()

    if request.method == "POST":
        # find title and author
        aut_title = {
            "title": request.form.get("title").title(),
            "author": request.form.get("author").title()
        }
        # find all book details
        book = {
            "image": request.form.get("image"),
            "title": request.form.get("title").title(),
            "author": request.form.get("author").title(),
            "genre": request.form.get("genre").title(),
            "added_by": session["user"].title(),
            "date": today
        }

        # check if book exists by checking title and author together
        existing_book = mongo.db.books.find_one(aut_title)

        # if it exists tell user the book is already in the DB
        if existing_book:
            flash("This book already exists.")

        # If it doesn't exist, add the book
        else:

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
        # get review details to add to DB
        review = {
            "author": request.form.get("author1").title(),
            "title": request.form.get("title").title(),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "review_by": session["user"].title()
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added. Thanks!")
        return redirect(url_for("browsebooks"))

    return render_template("addreview.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Allow user to search by author name / genre
    """
    # get query, find it in DB
    query = request.form.get("query")
    books = mongo.db.books.find({"$text": {"$search": query}})
    reviews = mongo.db.reviews.find()

    return render_template("books.html", books=books, reviews=list(reviews))


@app.route("/books")
def browsebooks():
    """
    Allow user to view books on system
    """
    # view books by most recent
    books = mongo.db.books.find().sort("date", -1)
    reviews = mongo.db.reviews.find()

    return render_template(
        "books.html", books=books, reviews=list(reviews))


@app.route("/viewreviews")
def viewreviews():
    """
    Allow user to see own reviews
    """
    # find all reviews then filtered with jinja
    reviews = mongo.db.reviews.find()

    return render_template("viewreviews.html", reviews=list(reviews))


@app.route("/viewbooks")
def viewbooks():
    """
    Allow user to see own reviews
    """
    # find all reviews then filtered with jinja
    books = mongo.db.books.find()

    return render_template("viewbooks.html", books=list(books))


@app.route("/edit/<review_id>", methods=["GET", "POST"])
def edit(review_id):
    """
    Allow user to edit their review
    """
    if request.method == "POST":
        # allow users to update a record
        update = {
            "title": request.form.get("title").title(),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "review_by": session["user"].title()
        }

        mongo.db.reviews.replace_one({"_id": ObjectId(review_id)}, update)
        flash("Review Updated")
        return redirect(url_for("viewreviews"))

    reviews = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    return render_template("edit.html", review=reviews)


@app.route("/editbook/<book_id>", methods=["GET", "POST"])
def editbook(book_id):
    """
    Allow user to edit their books
    """
    if request.method == "POST":
        # allow users to update a record
        update = {
            "image": request.form.get("image"),
            "title": request.form.get("title").title(),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "review_by": session["user"].title()
        }

        mongo.db.books.replace_one({"_id": ObjectId(book_id)}, update)
        flash("Book Updated")
        return redirect(url_for("viewbooks"))

    books = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("editbook.html", book=books)


@app.route("/delete/<review_id>", methods=["GET", "POST"])
def delete(review_id):
    """
    Allow user to delete a review
    """
    # find review
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Review removed")
    return redirect(url_for("userprofile", username=session['user']))


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
