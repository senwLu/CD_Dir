from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'itsSecret'

bcrypt = Bcrypt(app)

# if sessions does not have id, redirect to login page
# only allow access to login and signup page if no id in session


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
