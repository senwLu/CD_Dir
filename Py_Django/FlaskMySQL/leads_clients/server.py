from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)


@app.route('/')
def index():
    mysql = connectToMySQL("mydb")
    data_Table = mysql.query_db(
        "SELECT * FROM leads JOIN customers ON customers.id = leads.customer_id; ")

    # data_Table = {
    #     'Michael Choi': {'leads': 4},
    #     'Ryan Owen': {'leads': 7},
    #     'Joe Smitch': {'leads': 3},
    #     'Masaki Fujimoto': {'leads': 9}
    # }

    return render_template('index.html', data_Table=data_Table)


if __name__ == '__main__':
    app.run(debug=True)
