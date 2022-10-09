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

#show user
@app.route('/show/<int:user_id>')
def show(user_id):
    data = {
        'id' : user_id
    }
    return render_template('show.html', user=User.get_one(data))

#display user
@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    data = {
        'id' : user_id
    }
    return render_template('edit_user.html', user = User.get_one(data))


#edit user
@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    data = {
        'id' : user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect('/')




@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'id' : user_id
    }
    User.delete_user(data)
    return redirect('/')






if __name__ == '__main__':
    app.run(debug=True)
