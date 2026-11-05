from app.models import Pizza
from flask import make_response 
from flask_restful import Resource 

class Pizzas(Resource):
    def get(self):
        pizzas=[pizza.to_dict(rules=("-restaurant_pizzas",)) for pizza in Pizza.query.all()]

        return make_response(
            pizzas,200
        )