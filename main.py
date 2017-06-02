from flask import Flask, render_template, url_for, redirect, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.db_setup import Base, MenuItem, Restaurant

engine = create_engine('sqlite:///database/restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

session = DBSession()


app = Flask(__name__)


# Home page / index of all restaurants in the database
@app.route('/')
@app.route("/restaurants/")
def restaurant_index():
    restaurants = session.query(Restaurant).all()
    return render_template("restaurants.html", restaurants=restaurants)


# Create a new Restaurant
@app.route("/restaurant/new")
def new_restaurant():
    return "A place to create new restaurants"


# Edit an Existing Restaurant
@app.route("/restaurant/<int:restaurant_id>/edit")
def edit_restaurant(restaurant_id):
    return "Here we Edit the Restaurant"


# Delete an Existing Restaurant
@app.route("/restaurant/<int:restaurant_id>/delete")
def delete_restaurant(restaurant_id):
    return "Here we delete the Restaurant"


# An Index of all Menu Items for a given restaurant
@app.route("/restaurant/<int:restaurant_id>/menu")
def restaurant_menu(restaurant_id):
    return "A place to show all restaurant menu items"


# A Place to add a new menu item for a given restaurant
@app.route("/restaurant/<int:restaurant_id>/menu/new")
def new_menu_item(restaurant_id):
    return "here we add items to the menu"


# A Place to edit existing menu items for a given restaurant
@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit")
def edit_menu_item(restaurant_id, menu_id):
    return "A place to edit menu items"


# A Place to delete existing menu items for a given restaurant
@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete")
def delete_menu_item(restaurant_id, menu_id):
    return "A place to delete menu items"


if __name__ == '__main__':
    app.debug = True
    app.run()
