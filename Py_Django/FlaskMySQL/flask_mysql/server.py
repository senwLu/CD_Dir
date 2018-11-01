from flask import Flask, render_template, redirect, request
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
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
    mysql = connectToMySQL("flaskApp")
    query = "INSERT INTO users (username, created_at, updated_at) VALUES (%(username)s, NOW(), NOW());"
    data = {
        'username': request.form['username']
    }
    new_user_id = mysql.query_db(query, data)
    print(new_user_id)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
