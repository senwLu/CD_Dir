from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'itsSecret'

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    # if sessions does not have id, redirect to login page
    # only allow access to login and signup page if no id in session
    if session.get('user_id') == True:
        return render_template('index.html')
    else:
        return redirect('/login')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/dbList')
def db_page():
    if session.get('user_id') == True:
        return render_template('dbList.html')
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
