
from flask import render_template, Flask, request
import requests
import json


app = Flask(__name__)
app.secret_key = "123456"


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/driver', methods=['GET', 'POST'])
def driver():
    url = 'http://localhost:3000/api/org.seniordesign.vehicle.Vehicle'
    headers = {'Content-type': 'application/json'}
    data = '{"$class": "org.seniordesign.vehicle.Vehicle", "VIN": "93617", "type": "TRUCK", "crashLog": [] }'

    url2 = 'http://localhost:3000/api/org.seniordesign.crashLog.CreateCrashLog'
    headers2 = {'Content-type': 'application/json'}
    data2 = '{"$class": "org.seniordesign.crashlog.CreateCrashLog", "time": "2018-11-07T20:41:32.307Z", "speed": 88, "passengers": 2, "VIN": "93617", "airbagDeployment": true, "timestamp": "2018-11-07T20:41:32.308Z"}'

    url3 = 'http://localhost:3000/api/org.seniordesign.dailylog.CreateDailyLog'
    headers3 = {'Content-type': 'application/json'}
    data3 = '{"$class": "org.seniordesign.dailylog.CreateDailyLog", "timeSubmitted": "2018-11-28T01:18:27.225Z", "avgSpeed": 70, "totalDriveTimeMins": 240, "avgBrakingForce": 24, "avgAccelerationForce": 30, "VIN": "93617"}'

    url4 = 'http://localhost:3000/api/org.seniordesign.maintenance.CreateMaintenanceLog'
    headers4 = {'Content-type': 'application/json'}
    data4 =  '{"$class": "org.seniordesign.maintenance.CreateMaintenanceLog", "service": "OIL_CHANGE", "time": "2018-11-28T02:06:06.827Z", "mechID": "2421", "VIN": "93617"}'

    if request.method == 'POST':
        requests.post(url, data=data, headers=headers)
        requests.post(url2, data=data2, headers=headers2)
        requests.post(url3, data=data3, headers=headers3)
        requests.post(url4, data=data4, headers=headers4)

        return render_template('index.html')
    json_data = json.loads(data)
    json_data2 = json.loads(data2)

    return  render_template('driver.html', data=json_data, data2=json_data2)

@app.route('/police', methods=['GET'])
def police():
    url = 'http://localhost:3000/api/org.seniordesign.vehicle.Vehicle'
    response = requests.get(url)
    data = response.json()

    url2 = 'http://localhost:3000/api/org.seniordesign.dailylog.CreateDailyLog'
    response2 = requests.get(url2)
    data2 = response2.json()

    url3 = 'http://localhost:3000/api/org.seniordesign.maintenance.CreateMaintenanceLog'
    response3 = requests.get(url3)
    data3 = response3.json()



    return  render_template('police.html', data=data, data2=data2, data3=data3)


@app.route('/insurance', methods=['GET'])
def insurance():
    url = 'http://localhost:3000/api/org.seniordesign.crashLog.CrashLog'
    response = requests.get(url)
    data = response.json()

    return  render_template('insurance.html', data=data)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
# ====================