from wtforms import StringField, validators,SelectField, SubmitField
from flask_wtf import Form

class DailyLogForm(Form):
    speed = StringField('Speed', [validators.Length(min=1, max=10)])
    passengers = StringField('Passengers', [validators.Length(min=1, max=10)])
    airbag = SelectField('Deployed', choices=[('True', 'True'), ('False', 'False')])
    vin = StringField('VIN', [validators.Length(min=1, max=10)])
    submit = SubmitField('Submit')
