from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SelectField,FileField
from wtforms.validators import DataRequired,InputRequired
from flask_wtf.file import FileField,FileRequired,FileAllowed

class PropertyForm(FlaskForm):
    title=StringField('Property Title',validators=[DataRequired()])
    descrp=TextAreaField('Description',validators=[DataRequired()])
    no_bed=StringField('No. of Rooms',validators=[DataRequired()])
    no_bath=StringField('No. of Bathrooms',validators=[DataRequired()])
    price=StringField('Price',validators=[DataRequired()])
    types= SelectField('Property Type',[DataRequired()],choices=[('House','House'),('Apartment','Apartment')])
    location=StringField('Location',validators=[DataRequired()])
    photo= FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'],'Only image files')])