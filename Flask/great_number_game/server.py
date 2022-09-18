from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():

	if 'number' not in session:
		session['number'] = 0

	session['number'] = random.randrange(0,101)
	return render_template('index.html')

@app.route('/show', methods=['POST'])
def show():
	print("random num: ", session['number'])
	return render_template('show.html', guess = int(request.form['guess']), number = int(session['number']))

@app.route('/newgame', methods=['GET'])
def newgame():
	session.clear()

	return redirect('/')

# Server Listener
if __name__=="__main__":
    # run our server
    app.run(debug=True) 