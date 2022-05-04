from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Postcode:
    def __call__(self, form, field):
        try:
            int(field.data)
            if len(field.data) != 9:
                raise ValidationError("This is not a valid postcode")
        except ValueError:
            raise ValidationError("This is not a valid postcode")


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("Remember")


class RegisterForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8)])
    repeated_password = PasswordField("repeated_password", validators=[DataRequired(), EqualTo(password)])
    first_name = StringField("first_name", validators=[DataRequired()])
    last_name = StringField("second_name", validators=[DataRequired()])
    address = StringField("address", validators=[DataRequired()])
    postcode = StringField("postcode", validators=[DataRequired(), Postcode()])
    cart = StringField("cart", validators=[DataRequired()])
