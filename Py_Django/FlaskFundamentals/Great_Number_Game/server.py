from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'secretKEY'


@app.route('/')
def index():
    if 'guessNum' not in session:
        session['guessNum'] = random.randrange(100)

    if 'rtnStr' not in session:
        rtnStr = ""
    else:
        rtnStr = session['rtnStr']

    return render_template('index.html', rtnStr=rtnStr)


@app.route('/guess', methods=['POST'])
def guess():
    print(session['guessNum'])
    guess = int(request.form['guess'])
    if guess == session['guessNum']:
        session['rtnStr'] = "Correct!"
    elif guess > session['guessNum']:
        session['rtnStr'] = "To High!"
    elif guess < session['guessNum']:
        session['rtnStr'] = "To Low!"

    return redirect('/')


@app.route('/clearSession')
def clear():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
