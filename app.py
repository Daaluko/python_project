from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:password@localhost:5432/orangejuice"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.city_controller import cities_blueprint
from controllers.country_controller import countries_blueprint
from models import Country, City
app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)




@app.route('/')
def home():
    return render_template("/index.jinja")

@app.route('/mybucketlist')
def bucketlist():
    countries = Country.query.all()
    return render_template("/mybucketlist.jinja", countries=countries)

@app.route('/addcountry')
def addcountry():
    return render_template('countries/new.jinja')


@app.route('/addnewcity')
def addnewcity():
    countries = Country.query.all()
    return render_template('cities/new.jinja', countries = countries)
