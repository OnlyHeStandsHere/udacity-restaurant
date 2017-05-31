from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)


# Home page / index of all restaurants in the database
@app.route('/')
@app.route("/restaurants/")
def restaurant_index():
    return 'Home page for all restaurants'


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
    app.run()
