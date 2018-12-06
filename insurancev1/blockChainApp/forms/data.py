from wtforms import SubmitField
from flask_wtf import Form

class DataForm(Form):
    submit4 = SubmitField('View Data')