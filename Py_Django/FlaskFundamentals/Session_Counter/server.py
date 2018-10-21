from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1

    return render_template('index.html')


@app.route('/add2')
def add2():
    session['count'] += 2
    return redirect('/')


@app.route('/reset')
def reset():
    session['count'] = 1
    return redirect('/')


@app.route('/destory_session')
def destorySession():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
