from flask import Flask,  render_template, request, flash
import sqlite3

con = sqlite3.connect("tutorial.db", check_same_thread=False)
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
cur = con.cursor()

def add(nickname):
    cur.execute("INSERT INTO NICKNAMES (NICKNAME) VALUES(?)", (nickname,))
    con.commit()

def showlist():
    return 0

@app.route("/")
def index():
    add("Marek")
    flash("test")
    return render_template("index.html")

@app.route("/nicklist". methods=("POST"))
def nicklist():
    showlist()
    return render_template("index.html")


cur.close
con.close