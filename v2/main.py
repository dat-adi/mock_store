#!/usr/bin/python3
"""
This is the main file where the program runs from.
"""


from flask import Flask, redirect, render_template, url_for

# DB Functions that can do CRUD operations.
from db import Pet, DatabaseConnection

# Forms that can be used for the operations.
from forms import PetRegistrationForm, OwnerRegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
db_conn: DatabaseConnection = DatabaseConnection()


# Routes that can be contacted for the CRUD operations.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pets")
def get_pets():
    pets = db_conn.get_pets()
    print(pets)
    return render_template("get_pets.html", pets=pets)

@app.route("/pets/add", methods=["GET", "POST"])
def add_pet():
    form = PetRegistrationForm()
    if form.validate_on_submit():
        db_conn.add_pet(form)
        return redirect(url_for('index'))
    return render_template("add_pet.html", form=form)

@app.route("/pets/update/<id>", methods=["GET", "POST"])
def update_pet(id: int):
    form = PetRegistrationForm()

    if form.validate_on_submit():
        print([field.data for field in form])
        db_conn.update_pet(form)
        return redirect(url_for('get_pets'))

    specific_pet: Pet = db_conn.get_pet(id)

    form.id.data = specific_pet.get_id()
    form.name.data = specific_pet.get_name()
    form.animal.data = specific_pet.get_animal()
    form.price.data = specific_pet.get_price()
    form.owner_id.data = specific_pet.get_owner_id()

    return render_template("update_pet.html", form=form)

@app.route("/pets/delete/<id>")
def delete_pet(id: int):
    db_conn.delete_pet(id)
    return render_template("get_pets.html")


if __name__ == "__main__":
    db_conn.create_tables()
    app.run(debug=True)
