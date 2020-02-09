from flask import request, Flask, render_template, jsonify
import requests


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")




@app.route("/dash", methods=['POST'])
def dash():
    
    city = request.form.get("city")
        
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=4669e37f13c2c2c99aae6c323e53961d&units=metric'.format(city)

    #
    res = requests.get(url)
    data = res.json()

    temp = data['main']['temp']
    temp = int(temp)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    weather = data['weather'][0]['icon']

  
    
    return render_template ('index.html', city=city,temp=temp,pressure=pressure,humidity=humidity,wind_speed=wind_speed,weather=weather)

if __name__ == "__main__":
	app.run(threaded=True, debug=True)