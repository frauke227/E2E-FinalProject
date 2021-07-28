from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    languages = StringField('Spoken Languages', validators=[DataRequired()])
    specialisation = StringField ('Specialisation', validators=[DataRequired()])
    address = StringField('Adress', validators=[DataRequired()])
    lat = HiddenField('lat')
    lng = HiddenField('lng')
    phone = StringField('Phone Number')
    email = StringField('E-Mail Adress')
    website = StringField('Website')
    submit = SubmitField('Create new Profile')

  
class AddressForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = TextAreaField('Adress', validators=[DataRequired()])
    lat = HiddenField('lat')
    lng = HiddenField('lng')
    submit = SubmitField('Create new Profile')

  


