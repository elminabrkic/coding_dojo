from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "hello!"

@app.route("/play")
def play():
    return render_template("playground1.html")

@app.route("/play/<x>")
def play_repeat(x):
    repeat = int(x)
    return render_template("playground2.html", repeat = repeat)

@app.route("/play/<x>/<color>")
def play_color(x, color):
    repeat = int(x)
    change_color = color
    return render_template("playground3.html", repeat = repeat, change_color = change_color)

if __name__ == "__main__":
    app.run(debug = True)