from flask import Flask, render_template, send_file, request, redirect, url_for
from pathlib import Path
import sqlite3
import os
app=Flask(__name__)

con=sqlite3.connect("data.db")
try:
    con.execute("create table contact(name text,email text,subject text,message text)")
except: 
    pass
@app.route('/')
def index():
    return render_template("index.html")   

# @app.route('/download-resume')
# def download_resume():
#     # Assuming resume.pdf is stored in 'static/img' directory
#     resume_path = Path(__file__).parent / 'static' / 'image' / 'sreerajpr.pdf'
#     return send_file(resume_path, as_attachment=True) 


@app.route('/form', methods=['POST', 'GET'])
def fun1():
    if request.method == 'POST':
        name = request.form.get('name')  # Use get to avoid potential KeyError
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Insert data into the database
        con = sqlite3.connect('data.db')
        con.execute('INSERT INTO contact(name, email, subject, message) VALUES (?, ?, ?, ?)', (name, email, subject, message))
        con.commit()
        con.close()

        print(name, email, subject, message)
        return redirect(url_for('fun1'))  # Redirect after successful form submission

    # Render the form for GET requests
    return render_template("form.html")

# Start the Flask application
app.run()
