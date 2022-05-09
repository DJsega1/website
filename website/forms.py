from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, ValidationError, IntegerRangeField, TextAreaField
from wtforms import IntegerField, MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, regexp
import re


class Postcode:
    def __call__(self, form, field):
        try:
            int(field.data)
            if len(field.data) != 6:
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
    repeated_password = PasswordField("repeated_password", validators=[DataRequired(), EqualTo('password')])
    first_name = StringField("first_name", validators=[DataRequired()])
    last_name = StringField("second_name", validators=[DataRequired()])
    address = StringField("address", validators=[DataRequired()])
    postcode = StringField("postcode", validators=[DataRequired(), Postcode()])
    cart = StringField("cart", validators=[DataRequired()])


class AdminForm(FlaskForm):
    vendor_code = IntegerField("vendor_code", validators=[DataRequired()])
    name = StringField("title", validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
    price = IntegerField("price", validators=[DataRequired()])
    amount = IntegerField("amount", validators=[DataRequired()])
    brand = StringField("brand", validators=[DataRequired()])
    material = StringField("material", validators=[DataRequired()])
    color = StringField("color", validators=[DataRequired()])
    cloth_type = StringField("cloth_type", validators=[DataRequired()])
    sex = StringField("sex", validators=[DataRequired()])
    pictures = MultipleFileField("pictures", validators=[regexp('^\[^/\\\]\.jpg$')])

    @staticmethod
    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)
