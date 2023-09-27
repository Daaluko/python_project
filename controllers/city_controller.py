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
    countries = Country.query.all()
    return render_template("/cities/new.jinja", countries = countries)



@cities_blueprint.route("/cities", methods=["POST"])
def add_city():
    city_name = request.form["name"]
    country_id = request.form["country_id"]                                  # country_id = request.form.get("country.id")
    visited = request.form.get("visited")
    if visited == "on": visited = True 
    else: visited = False
    save_city= City(name=city_name, country_id=country_id, visited=visited)

    db.session.add(save_city)
    db.session.commit()
    return redirect("/mybucketlist")

@cities_blueprint.route("/cities/<int:id>/delete", methods=["POST"])
def delete_city(id):
    
    city = City.query.get(id)
    db.session.delete(city)
    db.session.commit()
    return redirect("/mybucketlist")


@cities_blueprint.route("/cities/<int:id>", methods=["POST"])
def update_city(id):
    city = City.query.get_or_404(id)
    city.visited = not city.visited
    db.session.commit()
    return redirect("/mybucketlist")

# @cities_blueprint.route("/cities/<int:id>", methods=["POST"])