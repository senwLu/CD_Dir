from flask import Flask  # Import Flask to allow us to create our app.

# Global variable __name__ tells Flask whether or not we are running the file
# directly, or importing it as a module.
app = Flask(__name__)

print(__name__)          # Just for fun, print __name__ to see what it is


# The "@" symbol designates a "decorator" which attaches the following
@app.route('/')
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response.


@app.route('/success')
def success():
    return "success"


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<strIn>')
def say(strIn):
    if strIn == 'john':
        return 'Hi John!'
    else:
        a = list(strIn)
        a[0] = a[0].upper()
        a = ''.join(a)
        return 'Hi ' + a + "!"


@app.route('/repeat/<times>/<reStr>')
def repeat(times, reStr):
    i = 0
    strResult = ""
    while i < int(times):
        strResult += reStr + " "
        i += 1
    return strResult


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "hello "+name


# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


# If __name__ is "__main__" we know we are running this file directly and not importing
# it from a different module
if __name__ == "__main__":

    app.run(debug=True)    # Run the app in debug mode.
