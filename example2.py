from flask import Flask, render_template

app = Flask("Example 2")

@app.route("/")
def index():
    return render_template(
        "example2.html",
        name="Pepe",
        occupation = "Teacher")

app.run()
