from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL


@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos=Dojo.get_all()
    return render_template('home.html', all_dojos=dojos)

@app.route("/toDojos", methods=["post"])
def toDojos():
    return redirect("/dojos")


@app.route("/create_dojo", methods=["post"])
def createDojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.create(data)
    return redirect("/dojos")

@app.route("/toNinjas", methods=["post"])
def toNinjas():
    thisid = request.form["id"]
    return redirect(f"/dojos/{thisid}")


# @app.route("/dojos/<id>")
# def dojosId(id):
#     names = Dojo.get_name(id)
#     name = names[0]["name"]
#     allNinjas = Ninja.showNinjasInDojo(id)
#     return render_template("dojo_show.html", allNinjas = allNinjas, myName = name)

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    } 
    a_dojo = Dojo.get_one_with_ninjas(data)
    return render_template("dojo_show.html", one_dojo=a_dojo)