from app.models import RestaurantPizza
from flask import request,make_response 
from app.db import db  
from flask_restful import Resource

class RestaurantPizzas(Resource):
    def post(self):
        data=request.get_json()

        allowed_fields=["price","pizza_id","restaurant_id"]

        restaurant_pizza=RestaurantPizza()

        if "price" in data  and "pizza_id" in data and "restaurant_id" in data:
            for attr,value in data.items():
                if attr in allowed_fields:
                    setattr(restaurant_pizza,attr,value)

            db.session.add(restaurant_pizza)
            db.session.commit()

            response = restaurant_pizza.to_dict()

            return make_response(response,201)


        return {"error":["validation errors"]},422

        
            
        