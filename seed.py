from app import db
from models.city import City
from models.country import Country
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    country1 = Country("Portugal")
    country2 = Country("Spain")
    country3 = Country("Germany")
    city1 = City("Lisbon")
    city2 = City("Porto")
    city3 = City("Madrid")
    city4 = City("Barcelona")
    city5 = City("Berlin")
    city6 = City("Munich")

    db.session.add(country1)
    db.session.add(country2)
    db.session.add(country3)
    
    db.session.add(city1)
    db.session.add(city2)
    db.session.add(city3)
    db.session.add(city4)
    db.session.add(city5)
    db.session.add(city6)
    db.session.commit()

