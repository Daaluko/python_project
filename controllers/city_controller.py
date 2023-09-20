from flask import Flask, request, redirect, render_template
from flask import Blueprint
from models.city import City
from models.country import Country
from app import db

cities_blueprint = Blueprint("cities",__name__)



@cities_blueprint.route("/cities", methods=["GET"])
def get_cities():
    cities_from_db = City.query.all()
    return render_template("/curvis.jinja", cities= cities_from_db)


@cities_blueprint.route("/cities/new", methods=["GET"]) #button
def new_city():
    return render_template("/cities/new.jinja")



@cities_blueprint.route("/cities/new", methods=["POST"]) #form on /cities/new.jinja
def add_city():
    city_name = request.form["name"]
    country_id = request.form["countries"]
    
    save_city= City(name=city_name, country_id=country_id)

    db.session.add(save_city)
    db.session.commit()
    return redirect("/curvis")

@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    City.query.get(id).delete()
    db.session.commit()
    return redirect("/curvis")


