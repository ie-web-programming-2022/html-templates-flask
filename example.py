from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # jinja
    return render_template(
        "home.html"
    )

@app.route("/about.html")
def about():
    return render_template(
        "about.html",
        price_per_tortita="15"
    )

app.run()