
from flask import render_template, Flask, request
import json
import requests
import pandas as pd


app = Flask(__name__)
app.secret_key = "123456"


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/driver', methods=['GET', 'POST'])
def driver():
    if request.method == 'POST':
        url = 'http://localhost:3000/api/org.seniordesign.vehicle.Vehicle'
        headers = {'Content-type': 'application/json'}

        data = '{"$class": "org.seniordesign.vehicle.Vehicle", "VIN": "9999", "type": "SUV", "crashLog": [] }'

        requests.post(url, data=data, headers=headers)

        return render_template('index.html')


    return  render_template('driver.html')

@app.route('/police', methods=['GET'])
def police():
    url = 'http://localhost:3000/api/org.seniordesign.vehicle.Vehicle'
    response = requests.get(url)
    data = json.dumps(json.loads(response))


    return  render_template('police.html', data=data)


@app.route('/insurance', methods=['GET'])
def insurance():
    url = 'http://localhost:3000/api/org.seniordesign.vehicle.Vehicle'
    response = requests.get(url)
    data = response.json()

    return  render_template('insurance.html', text=data)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
# ====================