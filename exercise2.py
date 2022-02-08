from flask import Flask, render_template

class BandMember:
    def __init__(self, name, role, picture):
        self.name = name
        self.role = role
        self.picture = picture


beatles = [
    BandMember("John", "Sings", "https://duckduckgo.com/i/108eacf6.jpg"),
    BandMember("Paul", "Plays bass guitar", "https://duckduckgo.com/i/5fe284d9.jpg"),
    BandMember("Ringo", "Plays the drums", "https://duckduckgo.com/i/1d5a1b86.png"),
    BandMember("George", "Plays the guitar", "https://duckduckgo.com/i/1290f0ba.jpg"),
]

app = Flask("Exercise 2")

@app.route("/")
def index():
    return render_template(
        "exercise2.html",
        band = beatles)

app.run()
