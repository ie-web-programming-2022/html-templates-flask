from flask import Flask, render_template

app = Flask("Exercise 1")


@app.route("/")
def index():
    return render_template(
        "exercise1.html",
        logged_in = True)

app.run()
