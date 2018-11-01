from flask import Flask, render_template, redirect, request
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# we are creating an object called bcrypt,
# which is made by invoking the function Bcrypt with our app as an argument
bcrypt = Bcrypt(app)

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('flaskApp')


@app.route('/')
def index():
    mysql = connectToMySQL("flaskApp")
    all_users = mysql.query_db("SELECT * FROM users")
    # print("Fetched all friends", all_friends)
    return render_template('index.html', users=all_users)


@app.route('/create_user', methods=['POST'])
def create():

    # include some logic to validate user input before adding them to the database!
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    mysql = connectToMySQL("flaskApp")

    # put the pw_hash in our data dictionary, NOT the password the user provided
    data = {
        'username': request.form['username'],
        'password_hash': pw_hash
    }

    query = "INSERT INTO users (username, password, created_at, updated_at) VALUES (%(username)s, %(password_hash)s, NOW(), NOW());"

    mysql.query_db(query, data)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
