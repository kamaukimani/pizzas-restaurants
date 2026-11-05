from app.models import Restaurant 
from flask_restful import Resource 
from flask import request,make_response 

class Restaurants(Resource):
    def get(self):
        restaurants=[restaurant.to_dict(rules=("-restaurant_pizzas",)) for restaurant in Restaurant.query.all()]

        return make_response(
            restaurants,200
        )