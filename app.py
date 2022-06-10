import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for) 
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if current_user:
            flash("This username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already in the database
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            # make sure hashed password matches user input
            if check_password_hash(
                user_exists["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # password does not match
                flash("Incorrect Username and/or Password, please try again")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Incorrect Username and/or Password, please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book_exists = mongo.db.books.find_one(
            {"title": request.form.get("title").lower()}
        )

        if book_exists:
            flash("This book already exists")
            return redirect(url_for("add_book"))
        else:
            book = {
                "title": request.form.get("title"),
                "author": request.form.get("author"),
                "genre_name": request.form.get("genre_name"),
                "synopsis": request.form.get("synopsis"),
                "cover_url": request.form.get("cover_url"),
                "added_by": session["user"]
            }
            mongo.db.books.insert_one(book)
            flash("Book Successfully Added")
            return redirect(url_for("get_books"))

    genres = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("add_book.html", genres=genres)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {"$set": {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre_name": request.form.get("genre_name"),
            "synopsis": request.form.get("synopsis"),
            "cover_url": request.form.get("cover_url"),
            "added_by": session["user"]
        }}
        mongo.db.books.update_one({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")
        return redirect(url_for("get_books"))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    genres = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("edit_book.html", book=book, genres=genres)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.delete_one({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genre.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genre.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {"$set": {
            "genre_name": request.form.get("genre_name")
        }}
        mongo.db.genre.update_one({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genre.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genre.delete_one({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)