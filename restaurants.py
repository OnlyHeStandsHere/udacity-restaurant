from flask import Flask, render_template, request, url_for, redirect, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Restaurant, Base, MenuItem

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




@app.route("/restaurants/<int:restaurant_id>/menu")
def restaurant_menu(restaurant_id):
    return "A place to show all restaurant menu items"

if __name__ == '__main__':
    app.run()
