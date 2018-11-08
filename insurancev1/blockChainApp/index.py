
from flask import render_template, Flask, request
import requests


app = Flask(__name__)
app.secret_key = "123456"


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/driver', methods=['GET', 'POST'])
def driver():
    url = 'http://localhost:3000/api/org.seniordesign.vehicle.Vehicle'
    headers = {'Content-type': 'application/json'}
    data = '{"$class": "org.seniordesign.vehicle.Vehicle", "VIN": "23", "type": "SUV", "crashLog": [] }'

    url2 = 'http://localhost:3000/api/org.seniordesign.crashLog.CreateCrashLog'
    headers2 = {'Content-type': 'application/json'}
    data2 = '{"$class": "org.seniordesign.crashlog.CreateCrashLog", "time": "2018-11-07T20:41:32.307Z", "speed": 0, "passengers": 0, "VIN": "2323", "airbagDeployment": true, "timestamp": "2018-11-07T20:41:32.308Z"}'

    if request.method == 'POST':
        requests.post(url, data=data, headers=headers)
        requests.post(url2, data=data2, headers=headers2)

        return render_template('index.html')

    return  render_template('driver.html', data=data, data2=data2)

@app.route('/police', methods=['GET'])
def police():
    url = 'http://localhost:3000/api/org.seniordesign.vehicle.Vehicle'
    response = requests.get(url)
    data = response.json()


    return  render_template('police.html', data=data)


@app.route('/insurance', methods=['GET'])
def insurance():
    url = 'http://localhost:3000/api/org.seniordesign.crashLog.CrashLog'
    response = requests.get(url)
    data = response.json()

    return  render_template('insurance.html', data=data)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
# ====================