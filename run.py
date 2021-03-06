import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)