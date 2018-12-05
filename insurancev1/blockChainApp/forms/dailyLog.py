from wtforms import StringField, validators,RadioField, SubmitField
from flask_wtf import Form

class DailyLogForm(Form):
    avgSpeed = StringField('Average Speed', [validators.Length(min=1, max=10)])
    totalTime = StringField('Total Time', [validators.Length(min=1, max=10)])
    brakeForce = StringField('Braking Force', [validators.Length(min=1, max=10)])
    accForce = StringField('Acceleration Force', [validators.Length(min=1, max=10)])
    vin = StringField('VIN', [validators.Length(min=1, max=10)])
    consent = RadioField('Consent', choices=[('Yes', 'Consent to share information')])
    submit3 = SubmitField('Submit')
