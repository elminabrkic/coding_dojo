from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('survey.html')

@app.route('/result', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", name=name, location=location, language=language, comment=comment)
if __name__ == "__main__":
    app.run(debug=True)