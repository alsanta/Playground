from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def threeAndBlue():
    return render_template("index.html", number = 3, color = 'rgb(50, 126, 131)')

@app.route('/play/<number>')
def anyAndBlue(number):
    return render_template("index.html", number = int(number), color = 'rgb(50, 126, 131)')

@app.route('/play/<number>/<color>')
def anyAndColor(number,color):
    return render_template("index.html", number = int(number), color = str(color))


if __name__=="__main__":
    app.run(debug=True)