from flask import Flask 
from .db import db,migrate 
from .config import Config 
from .models import *
from .routes import *
from flask_restful import Api

def create_app():

    app=Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    api=Api(app)

    api.add_resource(Restaurants,'/restaurants',endpoint="restaurants")
    api.add_resource(RestaurantById,'/restaurants/<int:id>',endpoint="restaurants_id")
    api.add_resource(Pizzas,'/pizzas',endpoint="pizzas")
    api.add_resource(RestaurantPizzas,'/restaurant_pizzas',endpoint="restaurant_pizzas")



    return app