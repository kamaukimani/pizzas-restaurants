from app.models import Restaurant 
from flask_restful import Resource 
from flask import request,make_response 
from app.db import db

class Restaurants(Resource):
    def get(self):
        restaurants=[restaurant.to_dict(rules=("-restaurant_pizzas",)) for restaurant in Restaurant.query.all()]

        return make_response(
            restaurants,200
        )

class RestaurantById(Resource):
    def get(self,id):
        restaurant=Restaurant.query.filter_by(id=id).first()

        if restaurant:
            response=restaurant.to_dict()

            return make_response(
                response,200
            )
        return {"error":"Restaurant not found"},404
    def delete(self,id):
        restaurant=Restaurant.query.filter_by(id=id).first()

        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()

            return {},204
            
        return {"error":"Restaurant not found"},404