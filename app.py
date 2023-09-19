from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:password@localhost:5432/orangejuice"
app.config["SQLALCHEMY_ECHO"]= True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

from models.city import City
from models.country import Country
from controllers.city_controller import cities_blueprint
from controllers.country_controller import countries_blueprint

app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)

@app.route('/')
@app.route('/home')
def home():
    return "Congrats!"