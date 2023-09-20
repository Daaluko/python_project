from models.city import City
from models.country import Country

country1 = Country(id=1, name="Portugal")
country2 = Country(id=2, name="Spain")
country3 = Country(id=3, name="Germany")
city1 = City(id=1, name="Lisbon", country_id=1, visited= True)
city2 = City(id=2, name="Porto", country_id=1, visited= True)
city3 = City(id=3, name="Madrid", country_id=2, visited= True)
city4 = City(id=4, name="Barcelona", country_id=2, visited= False)
city5 = City(id=5, name="Berlin", country_id=3, visited= False)
city6 = City(id=6, name="Munich", country_id=3, visited= False)

print("My first country:", country1.name)