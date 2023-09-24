from flask import Flask, request, redirect, render_template
from flask import Blueprint
from models import City, Country
from app import db

countries_blueprint = Blueprint("countries", __name__)
    

# @countries_blueprint.route("/countries/new", methods=["GET"]) #button
# def new_country():
    
#     countries = Country.query.all()
#     return render_template("/countries/new.jinja", countries=countries)

@countries_blueprint.route("/countries", methods=["POST"])
def add_country():
    country_name = request.form.get("name")

    save_country = Country(name=country_name)

    db.session.add(save_country)
    db.session.commit()
    return render_template("/cities/fornewcountry.jinja")

# @countries_blueprint.route("/countries/<int:id>/edit", methods=["GET"]) #button
# def edit_country(): 
#     return render_template("/countries/edit.jinja")

    
#<int:id> this is incase <id> doesn't work
@countries_blueprint.route("/countries/<id>", methods=["POST"]) #page
def update_country(id):
    changecountry_name = request.form["name"]
    country_to_be_edited = Country.query.get(id)
    country_to_be_edited.name = changecountry_name
    
    db.session.commit()
    return redirect("/mybucketlist")


@countries_blueprint.route('/countries/<id>')
def show(id):
    country = Country.query.get(id)
    cities = Country.query.join(City).filter(City.country_id == id)
    return render_template('/countries/show.jinja', country=country, cities=cities)