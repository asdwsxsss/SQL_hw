import psycopg2

def delete_db():
    cur.execute("""
            DROP TABLE person, Phone CASCADE;
            """)


def create_structure():
    cur.execute('''CREATE TABLE IF NOT EXISTS person(
            PersonID SERIAL Primary Key,
            name VARCHAR(60) not null,
            surname VARCHAR(60) not null,
            email VARCHAR(70) not null);

            CREATE TABLE IF NOT EXISTS Phone
            (number VARCHAR(11) NOT NULL Primary Key,
            PersonID INTEGER REFERENCES Person(PersonID))''')

def add_new_client(name, surname, email):
    cur.execute('''INSERT INTO Person(name, surname, email) VALUES(%s, %s, %s);''', (name, surname, email))

def add_phone_number(number, client_id):
    cur.execute('''INSERT INTO Phone(number, PersonID) VALUES(%s, %s);''', (number, client_id))


def change_clients_data(PersonID, name=None, surname=None, email=None, old_phone_number=None, new_phone_number=None):
    if name != None:
        cur.execute('''UPDATE person SET name = %s WHERE PersonID = %s;''', (name, PersonID,))
    elif surname != None:
        cur.execute('''UPDATE person SET surname = %s WHERE PersonID = %s;''', (surname, PersonID,))
    elif email != None:
        cur.execute('''UPDATE person SET email = %s WHERE PersonID = %s;''', (email, PersonID,))
    elif old_phone_number != None:
        cur.execute('''UPDATE phone SET number = %s WHERE number=%s;''', (new_phone_number, old_phone_number))


def delete_phone_number(phone_number):
    cur.execute('''DELETE FROM phone WHERE number=%s;''', (phone_number,))


def delete_client(person_id):
    cur.execute('''delete from phone where PersonID=%s;
    DELETE  FROM person WHERE PersonID=%s;''', (person_id, person_id,))


def find_client(name=None, surname=None, email=None, number=None):
    cur.execute('''SELECT person.personID FROM person
    JOIN phone ph on ph.personID=person.personID
    where name=%s or surname =%s or email=%s or number=%s;''', (name, surname, email, number,))



if __name__ == "__main__":
    with psycopg2.connect(database='postgres', user='postgres', password='Zxcvb425') as conn:
        with conn.cursor() as cur:
            delete_db()
            create_structure()
            add_new_client('Innokentiy', 'Petrov', 'spb@spb.ru')
            add_new_client('Hero', 'Klin', 'ninja@gmail.com')
            add_new_client('Mike', 'Tyson', '111@pk.com')
            add_new_client('Vasya', 'Pupkin', 'hj@rambler.ru')
            add_new_client('Aleksandra', 'Ivanova', 'abcde@mail.ru')

            add_phone_number('89995555555', 1)
            add_phone_number('45654565454', 1)
            add_phone_number('86565656565', 2)
            add_phone_number('89997778885', 4)
            add_phone_number('89779979752', 5)
            add_phone_number('89779979444', 5)

            change_clients_data('2', name='Hero')
            change_clients_data('2', old_phone_number='7', new_phone_number='5')

            delete_phone_number('45654565454')

            find_client(surname='Petrov')
            find_client(number='89997778885')
    conn.close()