from app import db

class City(db.Model):
    __tablename__="cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"))
    visited = db.Column(db.Boolean, default=True)
    # not_visited = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f"<City: id: {self.id}, name: {self.name}, country_id= {self.country_id}, visited= {self.visited} >"
    # not_visited= {self.not_visited}
class Country(db.Model):
    __tablename__="countries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    cities = db.relationship("City", backref="country")
    def __repr__(self):
        return f"<Country: id: {self.id}, name: {self.name}>"