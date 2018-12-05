from wtforms import StringField, validators,SelectField, SubmitField, RadioField
from flask_wtf import Form

class CrashLogForm(Form):
    speed = StringField('Speed', [validators.Length(min=1, max=10)])
    passengers = StringField('Passengers', [validators.Length(min=1, max=10)])
    airbag = SelectField('Airbag Deployed', choices=[('True', 'True'), ('False', 'False')])
    vin = StringField('VIN', [validators.Length(min=1, max=10)])
    consent = RadioField('Consent', choices=[('Yes', 'Consent to share information')])
    submit2 = SubmitField('Submit')
