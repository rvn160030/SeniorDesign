from wtforms import Form, StringField, validators, HiddenField, SelectMultipleField, widgets

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class VehicleForm(Form):
    id = HiddenField("org.seniordesign.vehicle.Vehicle")
    vin = StringField('VIN', [validators.Length(min=1, max=10)])

    string_of_types = ['TRUCK\r\nSUV\r\nVAN\r\nMINIVAN\r\nWAGON\r\nSEDAN\r\nCOUPE\r\nCABRIOLET\r\nROADSTER']
    list_of_types = string_of_types[0].split()

    types = [(x,x) for x in list_of_types]
    type = MultiCheckboxField('Type', choices=types)

