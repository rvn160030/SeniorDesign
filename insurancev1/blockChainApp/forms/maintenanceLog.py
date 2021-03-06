from wtforms import StringField, validators, SelectField, SubmitField, RadioField
from flask_wtf import Form


class MaintenanceLogForm(Form):
    service = SelectField('Service', choices=[('OIL_CHANGE', 'Oil Change'), ('TIRE_ROTATION', 'Tire Rotation')])
    mechID = StringField('Mechanic ID', [validators.Length(min=1, max=10)])
    vin = StringField('VIN', [validators.Length(min=1, max=10)])
    consent = RadioField('Consent', choices=[('Yes', 'Consent to share information')])

    submit4 = SubmitField('Submit')

