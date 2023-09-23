from app import db
from models import Country, City
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    country1 = Country(name="Portugal")
    country2 = Country(name="Spain")
    country3 = Country(name="Germany")
    city1 = City(name="Lisbon", visited= True, country_id=1)
    city2 = City(name="Porto", visited= True, country_id=1)
    city3 = City(name="Madrid", visited= True, country_id=2)
    city4 = City(name="Barcelona", visited= False, country_id=2)
    city5 = City(name="Berlin", visited= False, country_id=3)
    city6 = City(name="Munich", visited= False, country_id=3)

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

