from flask import Flask, request, redirect, render_template
from flask import Blueprint
from models.city import City
from models.country import Country
from app import db

cities_blueprint = Blueprint("cities",__name__)





@cities_blueprint.route("/cities/new", methods=["GET"])
def new_city():
    return render_template("/cities/new.jinja")



@cities_blueprint.route("/cities", methods=["POST"])
def add_city():
    city_name = request.form["name"]
    country_id = request.form["country_id"]
    
    save_city= City(name=city_name, country_id=country_id)

    db.session.add(save_city)
    db.session.commmit()
    return redirect("/cities")

@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    City.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect("/cities")