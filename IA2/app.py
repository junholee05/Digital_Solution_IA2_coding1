from flask import Flask, render_template, abort,request, session, redirect, url_for, flash
from IA2.forms import BasicForm
import sqlite3
from config import Config
app = Flask(__name__)
app.secret_key = 'hellomynameisjunho'
def get_db_connection():
    connection = sqlite3.connect(r"C:\Users\Junho Lee\PycharmProjects\Digital Solution IA2 coding\IA2\database.db")
    return connection
'''
@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def hello(data=None):
    form=BasicForm()
    if form.validate_on_submit():
        data = form.email.data
        conn = get_db_connection()
        conn.execute("INSERT INTO users (email) VALUES (?)", (data,))
        conn.commit()
        conn.close()
    return render_template("index.html", data=data, form=form)
'''
@app.route('/')
def index():
    print("index running")
    return render_template('index.html')


#all @app.routes for html's
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route ('/register',methods = ['GET','POST'])
def register():
    print("ddddd")
    if session.get('username'):
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('register.html')
    else:
        user_details = (
            request.form['firstName'],
            request.form['lastName'],
            request.form['email'],
            request.form['password']
        )
        print("User details collected")
    insertuser(user_details)
    session['username'] = request.form ['email']
    return render_template("login.html")

def insertuser(user_details):
    con = sqlite3.connect('northside.db')
    print("Connection to database successful")
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL
    Email TEXT NOT NULL
    Password TEXT NOT NULL''')
    print("Table created in database")
    sql_execute_string = 'INSERT INTO users(FirstName, LastName, Email, Password) VALUES(?,?,?,?)'
    c.execute(sql_execute_string, user_details)
    con.commit()
    con.close()


@app.route ('/reset_password')
def reset():
    return render_template('reset_password.html')

@app.route ('/book_a_dj')
def book_a_dj():
    return render_template('book_a_dj.html')

@app.route ('/find_my_event')
def find_my_event():
    return render_template('find_my_event.html')

@app.route ('/find_my_event_information')
def find_my_event_information():
    return render_template('find_my_event_information.html')

@app.route ('/find_a_song')
def find_a_song():
    return render_template('find_a_song.html')





#checking whether the new password and confirm password is the same
@app.route('/reset_password/<reset_token>', methods=['GET', 'POST'])
def reset_password_confirm(reset_token):
    if request.method == 'GET':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            # Passwords match, perform password reset logic here
            # ...

            flash('Password has been reset successfully.')
            return render_template('reset_password.html')

        flash('New password and confirm password do not match.')

    return render_template('reset_password.html')


if __name__ == '__main__':
    app.run(debug=True)









