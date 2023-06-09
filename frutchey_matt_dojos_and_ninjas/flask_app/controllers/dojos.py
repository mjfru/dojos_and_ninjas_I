from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# App routes below:

# Home page
@app.route("/")
def home():
    dojos = Dojo.get_all_dojos()
    return render_template("/dojos.html", dojos = dojos)

# Create a new dojo
@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["dojo_name"]
    }
    Dojo.create_dojo(data)
    return redirect("/")

# Show an individual Dojo
# @app.route("/dojo/<int:id>")
# def get_one_dojo(id):
#     data = {"id":id}
#     return render_template("dojo.html", dojo = Dojo.get_one_dojo(data))

# Show a dojo and its students
@app.route("/dojo/<int:dojo_id>")
def get_dojo_info(dojo_id):
    return render_template("dojo.html", dojo = Dojo.get_dojo_info(dojo_id))

# Landing page to create a new ninja
@app.route("/read/create_page")
def read_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("/ninjas.html", dojos = dojos)

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    data = {
    "dojo_id": request.form["dojo_id"],
    "first_name": request.form["first_name"],
    "last_name": request.form["last_name"],
    "age": request.form["age"]
    }
    Ninja.create_ninja(data)
    # return redirect("/")
    return redirect(f"/dojo/{request.form['dojo_id']}")
