from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

import re

app = Flask(__name__)
app.secret_key = 'itsSecret'

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    # if sessions does not have id, redirect to login page
    # only allow access to login and signup page if no id in session
    if session.get('user_id'):
        mysql = connectToMySQL("chat_wallDB")
        all_wall_chat = mysql.query_db("SELECT * FROM messages")
        return render_template('chat_wall.html', wall_messages=all_wall_chat)
    else:
        return redirect('/login')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/user_login', methods=['POST'])
def user_login():
    session.clear()

    mysql = connectToMySQL('chat_wallDB')

    loginCheck_query = 'SELECT * FROM users WHERE username like %(username)s'
    loginCheck_data = {'username': request.form['username']}
    result = mysql.query_db(loginCheck_query, loginCheck_data)

    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['user_id'] = result[0]['id']
            return redirect('/')
        else:
            flash('Password incorrect!', 'password')
            return redirect('/login')
    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/user_signup', methods=['POST'])
def user_signup():
    mysql = connectToMySQL('chat_wallDB')

    userCheck_query = 'SELECT * FROM users WHERE username like %(username)s;'
    userCheck_data = {"username": request.form["username"]}
    result = mysql.query_db(userCheck_query, userCheck_data)

    # checking if username is blank or less than 5 characters
    if len(request.form['username']) < 1:
        flash('Username can not be blank!', 'username')
    elif len(request.form['username']) < 5:
        flash('Username needs to be longer than 5 characters!', 'username')
    elif result:
        flash('Username already in use, pick another!', 'username')

    # checking if password is blank or less than 8 characters
    if len(request.form['password']) < 1:
        flash('Password can not be blank!', 'password')
    elif len(request.form['password']) < 8:
        flash('Password can not be less than 8 characters!', 'password')

    if '_flashes' in session.keys():
        return redirect('/signup')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])

        data = {
            'username': request.form['username'],
            'password_hash': pw_hash
        }

        mysql = connectToMySQL('chat_wallDB')
        query = "INSERT INTO users (username, password, created_at, updated_at) VALUES (%(username)s, %(password_hash)s, NOW(), NOW());"
        mysql.query_db(query, data)

        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
