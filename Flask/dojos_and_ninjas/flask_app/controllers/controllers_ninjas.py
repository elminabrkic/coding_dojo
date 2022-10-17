
from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja')
def ninjas():
    results=Dojo.get_all()
    return render_template('new_ninja.html', all_dojos=results)

@app.route("/toNinja", methods=["post"])
def toNinja():
    return redirect("/ninja")

@app.route('/showNinjas/<int:id>')
def showPage(id):
    data = {
        'id': id
    }
    return render_template('dojo_show.html', thisDojo = Ninja.showNinjasInDojo(data), oneDojo = Dojo.get_name(data))

@app.route("/createNinja", methods=["post"])
def createNinja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojos_id": request.form.get("inputSelect")
    }
    Ninja.create(data)
    return redirect("/dojos")