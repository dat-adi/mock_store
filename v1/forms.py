#!/usr/bin/python3
"""
This is a form class holder.
"""
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class AnimalForm(FlaskForm):
    """
    This is the form class for the registration of an animal.
    It contains the follow data fields,
    - ID
    - Name
    - Animal Type
    - Breed
    - Price
    - Owner ID
    """

    p_id: IntegerField = IntegerField(
        "Provide the ID for the animal: ", validators=[DataRequired()]
    )
    p_name: StringField = StringField(
        "Provide the name for the animal: ", validators=[DataRequired()]
    )
    p_animal_type: SelectField = SelectField(
        "Pick the animal type: ",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("buf", "Buffalo")],
        validators=[DataRequired()],
    )
    p_breed: StringField = StringField(
        "Provide the breed of the animal: ", validators=[DataRequired()]
    )
    p_price: IntegerField = IntegerField(
        "Provide the price of the animal: ", validators=[DataRequired()]
    )

    # TODO: There is a need for a validator in here.
    p_owner_id: IntegerField = IntegerField(
        "Give the Owner ID of the animal: ", validators=[DataRequired()]
    )

    submit: SubmitField = SubmitField("Submit")


class OwnerForm(FlaskForm):
    """
    This is the form class for the registration of a user/owner.
    It contains the follow data fields,
    - ID
    - Name
    - Address
    - Phone Number
    """

    o_id: IntegerField = IntegerField(
        "Provide the ID for the owner: ", validators=[DataRequired()]
    )
    o_name: StringField = StringField(
        "Provide the name of the owner: ", validators=[DataRequired()]
    )
    o_address: StringField = StringField(
        "Provide the address of the owner: ", validators=[DataRequired()]
    )
    o_phno: StringField = StringField(
        "Provide the phone number of the owner: ", validators=[DataRequired()]
    )
