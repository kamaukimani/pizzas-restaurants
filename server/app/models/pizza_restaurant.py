from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy import ForeignKey 
from app.db import db 
from sqlalchemy_serializer import SerializerMixin 

class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__="restaurant_pizzas"

    serialize_rules=("-pizza.restaurant_pizzas")

    id:Mapped[int]=mapped_column(primary_key=True)
    price:Mapped[int]

    pizza_id:Mapped[int]=mapped_column(ForeignKey("pizzas.id"))
    restaurant_id:Mapped[int]=mapped_column(ForeignKey("restaurants.id"))

    pizza:Mapped["Pizza"]=relationship(back_populates="restaurant_pizzas")
    restaurant:Mapped["Restaurant"]=relationship(back_populates="restaurant_pizzas")


    def __repr__(self):
        return f"<RestaurantPizza {self.price}>"
