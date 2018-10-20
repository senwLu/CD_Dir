from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/danger')
def danger():
    print('a user tried to visit /danger.  we have redirected the user to /')
    return redirect('/')


@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    name = request.form['name']
    location = request.form['dojoLocation']
    comment = request.form['comment']

    return render_template('result.html', name=name, location=location, comment=comment)


if __name__ == '__main__':
    app.run(debug=True)
