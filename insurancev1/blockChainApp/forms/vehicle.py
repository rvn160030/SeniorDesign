from wtforms import Form, StringField, validators, HiddenField, RadioField




class VehicleForm(Form):
    id = HiddenField("org.seniordesign.vehicle.Vehicle")
    vin = StringField('VIN', [validators.Length(min=1, max=10)])
    type = RadioField('Type', choices=[('TRUCK', 'TRUCK'), ('SUV', 'SUV'), ('VAN', 'VAN'), ('MINIVAN', 'MINIVAN'), ('WAGON', 'WAGON'), ('SEDAN', 'SEDAN'), ('COUPE', 'COUPE'), ('CABRIOLET', 'CABRIOLET'), ('ROADSTER', 'ROADSTER')])


