from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField, SelectMultipleField, FileField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    languages = SelectMultipleField("Languages", choices=[], validators=[DataRequired()])
    specialisation = StringField ('Specialisation', validators=[DataRequired()])
    address = StringField('Adress', validators=[DataRequired()])
    lat = HiddenField('lat')
    lng = HiddenField('lng')
    phone = StringField('Phone Number')
    email = StringField('E-Mail Adress')
    website = StringField('Website')
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Create new Profile')

class UpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    languages = SelectMultipleField("Languages", choices=[], validators=[DataRequired()])
    specialisation = StringField ('Specialisation', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    lat = HiddenField('lat')
    lng = HiddenField('lng')
    phone = StringField('Phone Number')
    email = StringField('E-Mail Adress')
    website = StringField('Website')
    submit = SubmitField('Update Profile')

class LangForm(FlaskForm):
    language = StringField('Language')
    submit = SubmitField('Save')

class AddressForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = TextAreaField('Adress', validators=[DataRequired()])
    lat = HiddenField('lat')
    lng = HiddenField('lng')
    submit = SubmitField('Create new Profile')

  


