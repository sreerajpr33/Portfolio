from flask import Flask,render_template, request, redirect, url_for
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
