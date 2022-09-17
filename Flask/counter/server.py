from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if 'count_key' not in session:
        print("Key doesn't exist")
        session['count_key'] = 1
    else:
        print("Key exists")
        session['count_key'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['count_key'] += 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
    



