from flask import Flask, request, redirect, render_template
from flask import Blueprint
from models import City, Country
from app import db

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/countries", methods=["POST"])
def add_country():
    country_name = request.form.get("name")

    save_country = Country(name=country_name)
    
    db.session.add(save_country)
    
    db.session.commit()
    return redirect("/mybucketlist")

@countries_blueprint.route("/countries/<id>/edit", methods=["GET"])
def edit_country(id): 
    country = Country.query.get(id)
    return render_template("/countries/edit.jinja", country=country)

    

@countries_blueprint.route("/countries/<int:id>", methods=["POST"]) 
def update_country(id):
    changecountry_name = request.form.get("name")
    country_to_be_edited = Country.query.get(id)
    country_to_be_edited.name = changecountry_name
    
    db.session.commit()
    return redirect("/mybucketlist")


@countries_blueprint.route("/countries/<id>")
def show(id):
    country = Country.query.get(id)
    cities = City.query.filter_by(country_id=id).all()
    return render_template('/countries/show.jinja', country = country, cities = cities)