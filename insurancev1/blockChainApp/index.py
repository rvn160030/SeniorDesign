
from flask import render_template, Flask, request, redirect, url_for
from flask_bootstrap import Bootstrap
import requests
import json
from forms.vehicle import VehicleForm
from forms.crashLog import CrashLogForm
from forms.dailyLog import DailyLogForm
from forms.maintenanceLog import MaintenanceLogForm
from forms.data import DataForm
import datetime

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "123456"




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/driver', methods=['GET', 'POST'])
def driver():
    views = ['Form', 'Drivers Data']
    form = VehicleForm(request.form)
    form2 = CrashLogForm(request.form)
    form3 = DailyLogForm(request.form)
    form4 = DataForm(request.form)
    if request.method == 'POST' and form4.submit4.data and form4.validate():
        url = 'http://localhost:3000/api/org.seniordesign.crashLog.CrashLog'
        response = requests.get(url)
        data = response.json()

        url2 = 'http://localhost:3000/api/org.seniordesign.dailylog.CreateDailyLog'
        response2 = requests.get(url2)
        data2 = response2.json()

        url3 = 'http://localhost:3000/api/org.seniordesign.maintenance.CreateMaintenanceLog'
        response3 = requests.get(url3)
        data3 = response3.json()

        return render_template('insurance.html', data=data, data2=data2, data3=data3)

    if request.method == 'POST' and form.submit.data and form.validate():
        vin = form.vin.data
        vtype = form.type.data
        url = 'http://localhost:3000/api/org.seniordesign.vehicle.Vehicle'
        headers = {'Content-type': 'application/json'}
        data = json.dumps({"$class": "org.seniordesign.vehicle.Vehicle", "VIN": vin, "type": vtype, "crashLog": [] })

        requests.post(url, data=data, headers=headers)
        return render_template('index.html')

    if request.method == 'POST' and form2.submit2.data and form2.validate():
        speed = form2.speed.data
        passengers = form2.passengers.data
        airbag = form2.airbag.data
        vin = form2.vin.data

        url = 'http://localhost:3000/api/org.seniordesign.crashLog.CreateCrashLog'
        headers = {'Content-type': 'application/json'}
        data = json.dumps({"$class": "org.seniordesign.crashlog.CreateCrashLog", "time": datetime.datetime.now(), "speed": speed, "passengers": passengers, "VIN": vin, "airbagDeployment": airbag, "timestamp": str(datetime.datetime.now())}, default=str)

        requests.post(url, data=data, headers=headers)
        return render_template('index.html')

    if request.method == 'POST' and form3.submit3.data and form3.validate():
        avgSpeed = form3.avgSpeed.data
        totalTime = form3.totalTime.data
        brakeForce = form3.brakeForce.data
        accForce = form3.accForce.data
        vin = form3.vin.data

        url = 'http://localhost:3000/api/org.seniordesign.dailylog.CreateDailyLog'
        headers = {'Content-type': 'application/json'}
        data = json.dumps({"$class": "org.seniordesign.dailylog.CreateDailyLog", "timeSubmitted": str(datetime.datetime.now()), "avgSpeed": avgSpeed, "totalDriveTimeMins": totalTime, "avgBrakingForce": brakeForce, "avgAccelerationForce": accForce, "VIN": vin}, default=str)

        requests.post(url, data=data, headers=headers)

        return render_template('index.html')

    return  render_template('driver.html', form=form, form2=form2, form3=form3, views=views, form4=form4)

@app.route('/police', methods=['GET'])
def police():
    url = 'http://localhost:3000/api/org.seniordesign.crashLog.CrashLog'
    response = requests.get(url)
    data = response.json()

    return  render_template('police.html', data=data)


@app.route('/insurance', methods=['GET'])
def insurance():
    url = 'http://localhost:3000/api/org.seniordesign.crashLog.CrashLog'
    response = requests.get(url)
    data = response.json()

    url2 = 'http://localhost:3000/api/org.seniordesign.dailylog.CreateDailyLog'
    response2 = requests.get(url2)
    data2 = response2.json()

    url3 = 'http://localhost:3000/api/org.seniordesign.maintenance.CreateMaintenanceLog'
    response3 = requests.get(url3)
    data3 = response3.json()

    return  render_template('insurance.html', data=data, data2=data2, data3=data3)

@app.route('/maintenance', methods=['GET', 'POST'])
def maintenance():
    url = 'http://localhost:3000/api/org.seniordesign.maintenance.CreateMaintenanceLog'
    response = requests.get(url)
    data = response.json()

    form = MaintenanceLogForm(request.form)

    if request.method == 'POST' and form.submit4.data and form.validate():
        service = form.service.data
        mechID = form.mechID.data
        vin = form.vin.data

        url = 'http://localhost:3000/api/org.seniordesign.maintenance.CreateMaintenanceLog'
        headers = {'Content-type': 'application/json'}
        data = json.dumps({"$class": "org.seniordesign.maintenance.CreateMaintenanceLog", "service": service, "time": str(datetime.datetime.now()), "mechID": mechID, "VIN": vin}, default=str)

        requests.post(url, data=data, headers=headers)

        return redirect(url_for('maintenance'))

    return  render_template('maintenance.html', form=form, data=data)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
# ====================