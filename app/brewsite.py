from flask import Flask, render_template as rt

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user="Salvador Felix")


@app.route("/breweries")
def breweries():
    return rt("breweries.html", user="Salvador Felix")


@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html", user="Salvador Felix")


@app.route("/about")
def about():
    return rt("about.html", user="Salvador Felix")


if __name__ == "__main__":
    app.run(debug=True)