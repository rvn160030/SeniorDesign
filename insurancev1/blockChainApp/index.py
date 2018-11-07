
from flask import render_template, Flask, request
import requests


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

        data = '{"$class": "org.seniordesign.vehicle.Vehicle", "VIN": "2323", "type": "SUV", "crashLog": [] }'

        requests.post(url, data=data, headers=headers)

        url = 'http://localhost:3000/api/org.seniordesign.crashLog.CreateCrashLog'
        headers = {'Content-type': 'application/json'}
        data = '{"$class": "org.seniordesign.crashLog.CreateCrashLog", "time": "2018-11-07T20:41:32.307Z", "speed": 86,' \
               '"passengers": 4, "VIN": "2323", "airbagDeployment": True, "timestamp":  "2018-11-07T20:41:32.307Z"}'

        requests.post(url, data=data, headers=headers)

        return render_template('index.html')


    return  render_template('driver.html')

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

    return  render_template('insurance.html', text=data)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
# ====================