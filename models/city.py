from app import db

class City(db.Model):
    __tablename__="cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"))
    visited = db.Column(db.Boolean)
    country = db.relationship("Country", backref="cities")
    def __repr__(self):
        return f"<City: id: {self.id}, name: {self.name}, country_id= {self.country_id}>"
    
