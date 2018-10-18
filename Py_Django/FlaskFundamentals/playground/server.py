from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play')
def index():
    return render_template('index.html', count=3)


@app.route('/play/<repNum>')
def moreBlocks(repNum):
    return render_template('index.html', count=int(repNum))


@app.route('/play/<repNum>/<setColor>')
def extraMoreBlocks(repNum, setColor):
    return render_template('index.html', count=int(repNum), color=setColor)


if __name__ == '__main__':
    app.run(debug=True)
