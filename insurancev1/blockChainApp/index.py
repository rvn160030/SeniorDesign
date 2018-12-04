
from flask import render_template, Flask, request
from flask_bootstrap import Bootstrap
import requests
import json
from forms.vehicle import VehicleForm
from forms.crashLog import CrashLogForm
from forms.dailyLog import DailyLogForm
from forms.maintenanceLog import MaintenanceLogForm
import datetime

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "123456"




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/driver', methods=['GET', 'POST'])
def driver():
    form = VehicleForm(request.form)
    form2 = CrashLogForm(request.form)
    form3 = DailyLogForm(request.form)
    form4 = MaintenanceLogForm(request.form)
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
        data = json.dumps({"$class": "org.seniordesign.crashlog.CreateCrashLog", "time": datetime.datetime.now(), "speed": speed, "passengers": passengers, "VIN": vin, "airbagDeployment": airbag, "timestamp": str(datetime.now())})

        requests.post(url, data=data, headers=headers)
        return render_template('index.html')

    if request.method == 'POST' and form3.submit3.data and form3.validate():

        return render_template('index.html')

    if request.method == 'POST' and form4.submit4.data and form4.validate():

        return render_template('index.html')



    return  render_template('driver.html', form=form, form2=form2, form3=form3, form4=form4)

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