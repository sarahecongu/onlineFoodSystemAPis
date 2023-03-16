from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from backend.db import db



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")


    db.init_app(app)
    # importing blue prints
    from backend.categories.controller import categories
    from backend.districts.controller import districts
    from backend.addresses.controller import addresses 
    from backend .users.controller import users
    from backend .regions.controller import regions
    from backend .orders.controller import orders
    from backend .fooditems.controller import fooditems
    from backend .sub_categories.controller import sub_categories


    #registering blueprin
    #     #registering blueprints    ts    
    app.register_blueprint(districts)
    app.register_blueprint(categories)
    app.register_blueprint(addresses)
    app.register_blueprint(orders)
    app.register_blueprint(fooditems)
    app.register_blueprint(regions)
    app.register_blueprint(users)
    app.register_blueprint(sub_categories)



   
    return app