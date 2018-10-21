from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route


@app.route('/users', methods=['POST'])
def create_user():

    # we'll talk about the following two lines after we learn a little more about forms
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']

    print(request.form)

    # redirects back to the '/' route
    return redirect('/show')


@app.route('/show')
def show_user():
    return render_template('user.html')


if __name__ == "__main__":
    # run our server
    app.run(debug=True)
