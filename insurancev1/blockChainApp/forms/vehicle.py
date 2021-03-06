from wtforms import StringField, validators, SelectField, RadioField, SubmitField
from flask_wtf import Form


class VehicleForm(Form):
    vin = StringField('VIN', [validators.Length(min=1, max=10)])
    type = SelectField('Type', choices=[('TRUCK', 'Truck'), ('SUV', 'Suv'), ('VAN', 'Van'), ('MINIVAN', 'Minivan'),
                                        ('WAGON', 'Wagon'), ('SEDAN', 'Sedan'), ('COUPE', 'Coupe'), ('CABRIOLET', 'Cabriolet'),
                                        ('ROADSTER', 'Roadster')])
    consent = RadioField('Consent', choices=[('Yes', 'Consent to share information')])
    submit = SubmitField('Submit')

