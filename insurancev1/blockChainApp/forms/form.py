from wtforms import SubmitField
from flask_wtf import Form

class FormView(Form):
    submit5 = SubmitField('View Form')