from app import db
from models import City, Country

country1 = Country(name="Portugal")
country2 = Country(name="Spain")
country3 = Country(name="Germany")
city1 = City(name="Lisbon", country_id=country1.id, visited= True)
city2 = City(name="Porto", country_id=country1.id, visited= True)
city3 = City(name="Madrid", country_id=country2.id, visited= True)
city4 = City(name="Barcelona", country_id=country2.id, visited= False)
city5 = City(name="Berlin", country_id=country3.id, visited= False)
city6 = City(name="Munich", country_id=country3.id, visited= False)

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
