from flask import Flask, request, redirect, render_template
from flask import Blueprint
from models import City, Country
from app import db

cities_blueprint = Blueprint("cities",__name__)



# @cities_blueprint.route("/cities")
# def view_cities():
#     cities = City.query.all()
#     return render_template("index.jinja", cities= cities)


@cities_blueprint.route("/cities/new", methods=["GET"]) #button
def new_city():
    return render_template("/cities/new.jinja")



@cities_blueprint.route("/cities", methods=["POST"]) #form on /cities/new.jinja
def add_city():
    city_name = request.form["name"]
    country_id = request.form.get("countries")
    visited = request.form.get(False)
    save_city= City(name=city_name, country_id=country_id, visited=visited)

    db.session.add(save_city)
    db.session.commit()
    return redirect("/mybucketlist")

@cities_blueprint.route("/cities/<int:id>/delete", methods=["POST"])
def delete_city(id):
    City.query.get(id).delete()
    db.session.commit()
    return redirect("/mybucketlist")


