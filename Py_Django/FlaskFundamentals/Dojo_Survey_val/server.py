from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'itsSecret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/danger')
def danger():
    print('a user tried to visit /danger.  we have redirected the user to /')
    return redirect('/')


@app.route('/result', methods=['POST'])
def result():
    if len(request.form['name']) < 1:
        flash('Name cannot be empty!')
    else:
        name = request.form['name']

    if len(request.form['comment']) >= 120:
        flash('Comment field is no longer than 120 characters!')
    else:
        comment = request.form['comment']

    location = request.form['dojoLocation']

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return render_template('result.html', name=name, location=location, comment=comment)


if __name__ == '__main__':
    app.run(debug=True)
