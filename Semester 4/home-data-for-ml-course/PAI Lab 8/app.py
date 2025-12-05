from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

JOKE_API = "https://official-joke-api.appspot.com/random_joke"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_joke")
def get_joke():
    joke_response = requests.get(JOKE_API)
    joke = joke_response.json()
    return jsonify(joke)

if __name__ == "__main__":
    app.run(debug=True)
