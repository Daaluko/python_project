from models.city import City
from models.country import Country

country1 = Country(id=1, name="Portugal")
country2 = Country(id=2, name="Spain")
country3 = Country(id=3, name="Germany")
city1 = City(id=1, name="Lisbon", country_id=country1.id, visited= True)
city2 = City(id=2, name="Porto", country_id=country1.id, visited= True)
city3 = City(id=3, name="Madrid", country_id=country2.id, visited= True)
city4 = City(id=4, name="Barcelona", country_id=country2.id, visited= False)
city5 = City(id=5, name="Berlin", country_id=country3.id, visited= False)
city6 = City(id=6, name="Munich", country_id=country3.id, visited= False)

cities = City.query.all()
countries = Country.query.all()
print(city1.name,"in",country1.name)
print(cities)