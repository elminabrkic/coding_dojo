from flask import Flask, request, render_template, redirect, session
from user import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)


@app.route('/new_user')
def new_user():
    return render_template('new_user.html')

@app.route('/home')
def home():
    return render_template('/')


@app.route('/create_user', methods=['POST'])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
