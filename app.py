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
from werkzeug.utils import secure_filename

# check for env.py file
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# set configurations
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
UPLOAD_FOLDER = "/workspace/books_for_you/static/images/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

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
        return redirect(url_for("userprofile", username=session["user"]))

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
    # get users username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("userprofile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # advise user they are logged out
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home_page"))


@app.route("/addbook", methods=["GET", "POST"])
def addbook():
    if request.method == "POST":
        book = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
        }
        mongo.db.books.insert_one(book)
        flash("Book successfully added. Thanks!")
        return redirect(url_for("home_page"))

    return render_template("addbook.html")


@app.route("/addreview", methods=["GET", "POST"])
def addreview():
    if request.method == "POST":
        review = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "review_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added. Thanks!")
        return redirect(url_for("home_page"))

    return render_template("addreview.html")


# allow image uploads
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/uploadimage", methods=["GET", "POST"])
def uploadimage():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            print(image)

            return redirect(request.url)

    return render_template("uploadimage.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
