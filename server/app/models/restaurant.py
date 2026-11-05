from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db import db 
from sqlalchemy_serializer import SerializerMixin 
from typing import List
from sqlalchemy.ext.associationproxy import association_proxy

class Restaurant(db.Model,SerializerMixin):
    __tablename__="restaurants"

    serialize_rules=("-restaurant_pizzas.restaurant",)

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    address:Mapped[str]

    restaurant_pizzas:Mapped[List["RestaurantPizza"]]=relationship(back_populates="restaurant",cascade="all,delete-orphan")

    pizzas=association_proxy("restaurant_pizzas","pizza",creator=lambda pizza_obj:RestaurantPizza(pizza=pizza_obj))

    def __repr__(self):
        return f"<Restaurant {self.name}>"