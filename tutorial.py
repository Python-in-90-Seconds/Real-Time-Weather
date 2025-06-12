from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def weather():
    city = "Tampa"
    latitude, longitude = 27.9475, 82.4584

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    data = requests.get(url).json()["current_weather"]

    return render_template_string(
        str(f"""city: {city}
            <br>
            temperature: {data["temperature"]}
            <br>
            windspeed: {data["windspeed"]}""")
    )

if __name__ == "__main__":
    app.run(debug=True)
