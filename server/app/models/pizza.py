from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db import db 
from sqlalchemy_serializer import SerializerMixin 
from typing import List
from sqlalchemy.ext.associationproxy import association_proxy

class Pizza(db.Model,SerializerMixin):
    __tablename__="pizzas"

    serialize_rules=("-restaurant_pizzas.pizza")

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    ingredients:Mapped[str]

    restaurant_pizzas:Mapped[List["RestaurantPizza"]]=relationship(back_populates="pizza",cascade="all,delete-orphan")

    restaurants=association_proxy("restaurant_pizzas","restaurant",creator=lambda restaurant_obj:RestaurantPizza(restaurant=restaurant_obj))

    def __repr__(self):
        return f"<Pizza {self.name}, {self.ingredients}>"