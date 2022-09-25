from random import random
from datetime import datetime
from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'This is my key'

@app.route('/')
def index():

    if 'gold' not in session:
        session['gold'] = 0
    elif 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    current_time = datetime.now()
    if request.form['building'] == 'farm':
        earns = random.randrange(9,21)
        session['gold'] += earns
        session['activities'].append("Earned " +str(earns)+" golds from the farm " + str(current_time))
    elif request.form['building'] == 'cave':
        earns = random.randrange(4,11)
        session['gold'] += earns
        session['activities'].append("Earned " +str(earns)+" golds from the cave! " + str(current_time))
    elif request.form['building'] == 'house':
        earns = random.randrange(1,6)
        session['gold'] += earns
        session['activities'].append("Earned " +str(earns)+" golds from the house! " + str(current_time))
    elif request.form['building'] == 'casion':
       earns = random.randrange(-51,51)
       session['gold'] += earns
       if earns > 0:
            session['activities'].append("Earned " +str(earns)+" golds from the casion! " + str(current_time))
       else:
        session['activities'].append("Lost" +str(earns) +" golds from the casino! " +str(current_time))
    return redirect('/')

@app.route('/clear')
def clear():
    session['activities']=[]
    session['gold']=0
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)