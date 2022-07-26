"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from .utils import APIException, generate_sitemap
from .db import db
from .admin import setup_admin




#from models import Person
ENV = os.getenv("FLASK_ENV")
#static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../public/')
app = Flask(__name__)
app.url_map.strict_slashes = False
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#MIGRATE = Migrate(app, db)
#db.init_app(app)
##CORS(app)
#setup_admin(app)
##from src.rutas import enviarcorreo #Aquí importamos las rutas registradas en el __init__.py de la carpeta rutas

# database condiguration
DB_URL = os.getenv("DATABASE_URL")
if DB_URL is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db, compare_type = True)
db.init_app(app)
CORS(app)
setup_admin(app)
from src.modelos import User #Aquí importamos los modelos registrador en el __init__.py de la carpeta modelos
from src.rutas import enviarcorreo, register_user #Aquí importamos las rutas registradas en el __init__.py de la carpeta rutas

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3340))
    app.run(host='0.0.0.0', port=PORT, debug=False)
