from flask import Flask
import sqlite3
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash,generate_password_hash
import db
import config
import items

app=Flask(__name__)
app.secret_key = config.secret_key
db.initialize()
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/new_item")
def new_item():
    if "user_id" not in session:
        session.clear()
        return redirect("/login")
    return render_template("new_item.html")
    
    

@app.route("/create_item", methods=["POST"])
def create_item():
    if "user_id" not in session:
        session.clear()
        return redirect("/login")

    title = request.form["title"]
    artist = request.form["artist"]
    rating = request.form["rating"]
    comment = request.form["comment"]
    user_id = session["user_id"]
    items.add_item(title, artist, rating, comment, user_id)


    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result=db.query(sql,[username])[0]
        user_id=result["id"]
        password_hash=result["password_hash"]
        

        if check_password_hash(password_hash, password):
            session["user_id"]=user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")