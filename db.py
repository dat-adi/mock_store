#!/usr/bin/python3
"""
This file is in-charge of handling all the DB related operations.

@author: G V Datta Adithya
"""
import psycopg2


class Pet:
    """
    Class to centralize information of a singular pet.
    """

    def __init__(
        self,
        p_id: int,
        p_name: str,
        p_animal_type: str,
        p_breed: str,
        p_price: int,
        p_owner_id: int,
    ) -> None:
        self.id = p_id
        self.name = p_name
        self.animal_type = p_animal_type
        self.breed = p_breed
        self.price = p_price
        self.owner_id = p_owner_id

    def get_id(self) -> int:
        """
        Returns Pet ID.
        """
        return self.id

    def get_name(self) -> str:
        """
        Returns Pet Name.
        """
        return self.name

    def get_animal_type(self) -> str:
        """
        Returns Animal Type.
        """
        return self.animal_type

    def get_breed(self) -> str:
        """
        Returns Pet Breed.
        """
        return self.breed

    def get_price(self) -> int:
        """
        Returns the price of the Pet.
        """
        return self.price

    def get_owner_id(self) -> int:
        """
        Returns the Owner ID.
        """
        return self.owner_id


class DB:
    """
    This is a database class that consists of CRUD operations for Pets.
    """

    def __init__(self) -> None:
        """
        Initializing the name of the table, if it needs to be used in the
        table creation.
        """
        self.table_name = "Pets"

    @classmethod
    def connect_db(cls) -> None:
        """
        This is a method that connects the class to the database.
        """
        # TODO: Protect secrets
        cls.conn = psycopg2.connect(
            database="postgres", user="postgres", password="Finserv@2023"
        )
        cls.cur = cls.conn.cursor()

    @classmethod
    def create_table(cls) -> None:
        """
        This is a method that creates the tables for the `Owners` and the
        `Pets` classes.
        """
        cls.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS Owners (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    address VARCHAR(100),
                    ph_no VARCHAR(10)
                    );
                """
        )

        cls.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS Pets (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(20),
                    animal_type VARCHAR(10),
                    breed VARCHAR(20),
                    price INT,
                    owner_id INT REFERENCES Owners (id)
                    );
                """
        )

        cls.conn.commit()

    @classmethod
    def get_pets_from_db(cls) -> list:
        """
        This function is responsible for retrieving the pets from the
        database and returning a list of the different records.
        """
        cls.cur.execute(
            """
                SELECT *
                FROM Pets;
                """
        )
        pets = cls.cur.fetchall()

        return pets

    @classmethod
    def get_pet(cls, pet_id: int):
        """
        Gets a single pet from the database based on
        the `id` attribute.
        """
        cls.cur.execute(
            f"""
                SELECT *
                FROM Pets
                WHERE id={pet_id};
                """
        )

        return cls.cur.fetchone()

    @classmethod
    def add_pet_to_db(cls, pet: Pet) -> None:
        """
        Adds a pet to the database through insertion.
        """
        cls.cur.execute(
            """
                INSERT INTO Pets
                VALUES (%s, %s, %s, %s, %s, %s);
                """,
            (pet.id, pet.name, pet.animal_type, pet.breed, pet.price, pet.owner_id),
        )

        cls.conn.commit()

    @classmethod
    def update_pet_in_db(cls, pet: Pet) -> None:
        """
        Updates the details of a pet in the database.
        """
        cls.cur.execute(
            """
                UPDATE Pets
                SET name = %s,
                    animal_type = %s,
                    breed = %s,
                    price = %s,
                    owner_id = %s
                WHERE id = %s;
                """,
                (pet.name, pet.animal_type, pet.breed, pet.price, pet.owner_id, pet.id)
        )

        cls.conn.commit()

    @classmethod
    def delete_pet_in_db(cls, p_id: int) -> None:
        """
        Deletes a pet from the database.
        """
        cls.cur.execute(
            f"""
                DELETE FROM Pets
                WHERE id = '{p_id}';
                """
        )

        cls.conn.commit()
