from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp

class RegistrationForm(FlaskForm):
    name = StringField(
        'Name', 
        validators=[
            DataRequired(message="Name is required."),
            Length(min=3, max=50, message="Name must be between 3 and 50 characters."),
            Regexp(r'^[A-Za-z\s]+$', message="Name can only contain letters and spaces.")
        ]
    )
    email = StringField(
        'Email', 
        validators=[DataRequired(message="Email is required."), Email(message="Invalid email address.")]
    )
    submit = SubmitField('Register')
