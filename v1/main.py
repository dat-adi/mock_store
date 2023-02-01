#!/usr/bin/python3
"""
This piece of code is the main application file and consists of the routes
and the calls that are to be made to the different components.

@author: G V Datta Adithya
"""
from flask import Flask, redirect, render_template, url_for, request
from forms import AnimalForm
from db import Pet, DB


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


@app.route("/")
def index() -> str:
    """
    Welcome page for the Pet store website.
    """
    return render_template("index.html")


@app.route("/get_pets")
def get_pets() -> str:
    """
    Returning the different pets present in the Pet store.
    """
    try:
        pet_db: DB = DB()
        pet_db.connect_db()
        return render_template("get_pets.html", pets=pet_db.get_pets_from_db())
    except Exception as err:
        return str(err)


@app.route("/add_pet", methods=["GET", "POST"])
def add_pet():
    """
    Adding a Pet into the Pet store.
    """
    form: AnimalForm = AnimalForm()

    if form.validate_on_submit():
        pet: Pet = Pet(
            form.p_id.data,
            form.p_name.data,
            form.p_animal_type.data,
            form.p_breed.data,
            form.p_price.data,
            form.p_owner_id.data,
        )
        pet_db: DB = DB()
        try:
            pet_db.connect_db()
            pet_db.create_table()
            pet_db.add_pet_to_db(pet)
        except Exception as err:
            return str(err)
        return redirect(url_for("get_pets"))
    return render_template("add_pet.html", form=form)

def get_pet_info(p_id, form):
    pet_db: DB = DB()
    pet_db.connect_db()

    try:
        pet = pet_db.get_pet(p_id)
    except TypeError:
        return redirect(url_for("index"))
    except Exception as err:
        return str(err)

    form.p_id.data = pet[0]
    form.p_name.data = pet[1]
    form.p_animal_type.data = pet[2]
    form.p_breed.data = pet[3]
    form.p_price.data = pet[4]
    form.p_owner_id.data = pet[5]

    return form

@app.route("/update_pet/<p_id>", methods=["GET", "POST"])
def update_pet(p_id: int):
    """
    Update a Pet in the store based on the ID.
    """

    form: AnimalForm = AnimalForm()
    pet_db: DB = DB()
    pet_db.connect_db()

    form = get_pet_info(p_id, form)

    if form.validate_on_submit():
        print("Doesn't work")
        pet: Pet = Pet(
            form.p_id.data,
            form.p_name.data,
            form.p_animal_type.data,
            form.p_breed.data,
            form.p_price.data,
            form.p_owner_id.data,
        )
        try:
            pet_db.update_pet_in_db(pet)
        except TypeError as err:
            return str(err)

        return redirect(url_for("get_pets"))

    return render_template("update_pet.html", form=form)


@app.route("/delete_pet/<p_id>", methods=["GET", "POST"])
def delete_pet(p_id: int) -> str:
    """
    Delete a pet from the store.
    """
    try:
        pet_db: DB = DB()
        pet_db.connect_db()
        pet_db.delete_pet_in_db(p_id)
    except Exception as err:
        return f"Looks like the deletion didn't work for the following reason: {err}"
    return render_template("delete_pet.html")


if __name__ == "__main__":
    app.run(debug=True)
