from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    database = mongo.db.mars.find_one()
    # Return template and data
    return render_template("index.html", marsfinal=database)

@app.route("/scrape")
def scrape():
  
    mars_scrape = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update_one({}, {"$set":mars_scrape}, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=False)