# Corinne Bradford
# Sept 2021

from flask import *
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/breakfast")
def breakfast():
    return render_template("breakfast.html")

@app.route("/lunch")
def lunch():
    return render_template("lunch.html")

@app.route("/dinner")
def dinnner():
    return render_template("dinner.html")

@app.route("/food_trucks-taphouses")
def trucks_taphouses():
    return render_template("food_trucks-taphouses.html")

@app.route("/brewpubs")
def brewpubs():
    return render_template("brewpubs.html")

@app.route("/cideries")
def cideries():
    return render_template("cideries.html")

@app.route("/bars")
def bars():
    return render_template("bars.html")

@app.route("/summer")
def summer():
    return render_template("summer.html")

@app.route("/winter")
def winter():
    return render_template("winter.html")

@app.route("/indoor")
def indoor():
    return render_template("indoor.html")

@app.route("/dog_parks")
def dog_parks():
    return render_template("dog_parks.html")

if __name__ == "__main__":
    app.run(debug=True)