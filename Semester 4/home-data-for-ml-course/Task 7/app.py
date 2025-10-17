from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
API_KEY = "1851b16d52ff0cbee09f06dad2d9799f"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", "Lahore")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

@app.route("/")
def home():
    city = request.args.get("city", "Lahore")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render_template("index.html", weather=data)
    else:
        return render_template("index.html", weather=None)

if __name__ == "__main__":
    app.run(debug=True)
