from flask import Flask,render_template
import sqlite3
app=Flask(__name__)

con=sqlite3.connect("data.db")
try:
    con.execute("create table contact(name text,email text,subject text,message text)")
except: 
    pass
@app.route('/')
def index():
    return render_template("index.html")    
app.run()