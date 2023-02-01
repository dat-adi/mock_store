import psycopg2


class Pet:
    """
    The class for a Pet.
    Attributes,
    - id
    - name
    - animal
    - price
    - owner_id
    """
    def __init__(self, id: int, name: str, animal: str, price: int, owner_id: int):
        self.id: int = id
        self.name: str = name
        self.animal: str = animal
        self.price: int = price
        self.owner_id: int = owner_id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_animal(self):
        return self.animal

    def get_price(self):
        return self.price

    def get_owner_id(self):
        return self.owner_id


class DatabaseConnection:
    """
    The database connection class.
    """
    def __init__(self):
        self.conn = psycopg2.connect(
                database="postgres",
                user="postgres",
                password="Finserv@2023"
                )
        self.cur = self.conn.cursor()

    def get_connection(self):
        return self.conn
    
    def get_cursor(self):
        return self.cur

    def create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS Owners (
                id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                phone VARCHAR(10)
                );
        CREATE TABLE IF NOT EXISTS Pets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                animal VARCHAR(20),
                price INTEGER,
                owner_id INT REFERENCES Owners(id)
                );
        """

        self.cur.execute(query)
        self.conn.commit()

    def get_pet(self, id: int):
        query = f"""
        SELECT *
        FROM Pets
        WHERE id = {id};
        """

        self.cur.execute(query)
        return make_pet_from_tuple(self.cur.fetchone())

    def get_pets(self):
        query = """
        SELECT * 
        FROM Pets;
        """

        self.cur.execute(query)
        return self.cur.fetchall()


    def add_pet(self, form):
        pet_info: tuple = get_pet_info_from_form(form)

        query = """
        INSERT INTO Pets
        VALUES (%s, %s, %s, %s, %s);
        """

        self.cur.execute(query, pet_info)
        self.conn.commit()

    def update_pet(self, form):
        pet_info: tuple = get_pet_info_from_form_update(form)

        query = """
        UPDATE Pets
        SET name = %s,
            animal = %s,
            price = %s,
            owner_id = %s
        WHERE id = %s;
        """

        self.cur.execute(query, pet_info)
        self.conn.commit()

    def delete_pet(self, pet_id):
        query = """
        DELETE FROM Pets
        WHERE id = %s;
        """

        self.cur.execute(query, pet_id)
        self.conn.commit()

def get_pet_info_from_form_update(form) -> tuple:
    """
    A helper function to parse input from a form.
    """
    return (
        form.name.data, 
        form.animal.data, 
        form.price.data, 
        form.owner_id.data,
        form.id.data
        )

def get_pet_info_from_form(form) -> tuple:
    """
    A helper function to parse input from a form.
    """
    return (
        form.id.data, 
        form.name.data, 
        form.animal.data, 
        form.price.data, 
        form.owner_id.data
        )

def make_pet_from_tuple(info) -> Pet:
    """
    A helper function to make a Pet class from a tuple.
    """

    return Pet(
            info[0],
            info[1],
            info[2],
            info[3],
            info[4]
            )
