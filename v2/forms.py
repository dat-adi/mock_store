from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField


class PetRegistrationForm(FlaskForm):
    """
    This is the registration form for an animal.
    Attributes,
    - id
    - name
    - animal
    - price
    - owner_id
    """

    id: IntegerField = IntegerField("Animal ID: ")
    name: StringField = StringField("Animal Name: ")
    animal: SelectField = SelectField(
        "Animal Type: ", choices=[("cat", "Cat"), ("dog", "Dog"), ("ele", "Elephant")]
    )
    price: IntegerField = IntegerField("Price: ")
    owner_id: IntegerField = IntegerField("Owner ID: ")
    submit: SubmitField = SubmitField("Submit")


class OwnerRegistrationForm(FlaskForm):
    """
    This is the registration form for an owner.
    - id
    - name
    - phone
    """

    id: IntegerField = IntegerField("Owner ID: ")
    name: StringField = StringField("Owner Name: ")
    phone: StringField = StringField("Phone Number : ")
    submit: SubmitField = SubmitField("Submit")
