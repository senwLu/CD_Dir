from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'aSecret'

DIGIT_CHECK_REG = re.compile(r'\d')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
UPPER_CHAR_REG = re.compile(r'[A-Z]')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['conf_password']) < 1:
        flash('All fields are required and must not be blank')

    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email should be a valid email')

    if DIGIT_CHECK_REG.search(request.form['first_name']) or DIGIT_CHECK_REG.search(request.form['last_name']):
        flash('First and Last Name cannot contain any numbers')

    if len(request.form['password']) < 8:
        flash('Password should be more than 8 characters')
    elif UPPER_CHAR_REG .search(request.form['password']) == None or DIGIT_CHECK_REG .search(request.form['password']) == None:
        flash('Password must have at least 1 uppercase letter and 1 numeric value')
    elif request.form['password'] != request.form['conf_password']:
        flash('Password and Password Confirmation should match')

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return render_template('')


if __name__ == '__main__':
    app.run(debug=True)
