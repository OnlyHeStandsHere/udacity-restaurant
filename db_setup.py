import sys

from sqlalchemy import Column, Integer, ForeignKey, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):

    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    menu_items = relationship("MenuItem", backref="restaurant")

    def __repr__(self):
        return '<Restaurant:{}>'.format(self.name)


class MenuItem(Base):

    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    desc = Column(String(250))
    price = Column(String(8))
    course = Column(String(50))
    restaurant_id = Column(Integer, ForeignKey(Restaurant.id))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'price': self.price,
            'course': self.course,
            'restaurant_id': self.restaurant_id
        }

    def __repr__(self):
        return '<MenuItem:{}>'.format(self.name)


engine = create_engine(
    "sqlite:///restaurantmenu.db")

Base.metadata.create_all(engine)
