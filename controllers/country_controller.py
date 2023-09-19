from flask import Flask, request, redirect, render_template
from flask import Blueprint
from models.city import City
from models.country import Country
from app import db

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries/new", methods=["GET"])
def new_country():
    return render_template("/countries/new.jinja")

@countries_blueprint.route("/countries", methods=["POST"])
def add_country():
    country_name= request.form["name"]

    save_country= Country(name=country_name)

    db.session.add(save_country)
    db.session.commit()
    return redirect("/countries")

@countries_blueprint.route("/countries/<id>/edit", methods=["GET"])
def edit_country(): 
    return render_template("/countries/edit.jinja")

    

@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    changecountry_name = request.form["name"]
    
    newcountry_name = Country(name=changecountry_name)

    Country.query.filter_by(id = id).update(newcountry_name)
    db.session.commit()
    return redirect("/countries")