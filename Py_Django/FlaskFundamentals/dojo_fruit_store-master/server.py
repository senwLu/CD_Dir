from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    apple = request.form['apple']
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    studentId = request.form['student_id']
    total = int(apple)+int(strawberry)+int(raspberry)
    return render_template("checkout.html", apple=apple, strawberry=strawberry, raspberry=raspberry,
                           firstName=firstName, lastName=lastName, id=studentId, total=total)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
