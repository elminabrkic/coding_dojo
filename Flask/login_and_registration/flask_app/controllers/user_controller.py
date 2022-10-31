from flask import render_template, redirect, request, session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.users import User


bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page")
def page():
    return render_template("page.html")


@app.route("/register_user", methods = ["POST"])
def register_user():
    if 'user_id' not in session:
        return redirect("/")
    data ={
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password'],
    }
    valid = User.validate_user(data)
    print("valid", valid)
    if valid:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data['pw_hash'] = pw_hash
        user = User.create_user(data)
        session['user_id'] = user
        print('You got it!')
        return redirect('/page')
    return redirect('/')

@app.route('/login_user', methods=['POST'])
def login_user():
    if 'user_id' not in session:
        return redirect("/")
    
    user = User.get_by_email(request.form)
    if not user:
        flash('Invalid email or password')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid email or password')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('page.html')

    




