import sqlite3 as sq
from pprint import pprint

def create_db(file_name):
    with sq.connect(file_name) as file: # id INTEGER PRIMARY KEY AUTOINCREMENT,
        cur = file.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS people(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                country TEXT,
                                age INTEGER
                                )""")
    

def drop_table_in_file(file_name):
    with sq.connect(file_name) as file: # id INTEGER PRIMARY KEY AUTOINCREMENT,
        cur = file.cursor()
        cur.execute("DROP TABLE IF EXISTS people")



def write_in_file(file_name, lst):
    with sq.connect(file_name) as file:
        cur = file.cursor()
        cur.executemany("""INSERT INTO people
                                    (name, country, age)
                                    VALUES (:name, :country, :age)"""
                                  , lst)



def read_from_file(file_name, **kwargs):
    kwargs = dict(filter(lambda x: x[0] in COLUMNS_NAME, kwargs.items()))
    with sq.connect(file_name) as file:
        cur = file.cursor()
        query = "SELECT id, name, country, age FROM people"
        if kwargs:
            query += " WHERE " + " AND ".join(f"{k} = '{v}'" for k, v in kwargs.items())
        query += " ORDER BY country, age"
        cur.execute(query)
        return cur.fetchall()


def update_from_file_by_id(file_name, id, **kwargs):
    with sq.connect(file_name) as file:
        cur = file.cursor()
        query = "UPDATE people SET " + ", ".join(f"{k} = '{v}'" for k, v in kwargs.items())
        # query += " WHERE " + " AND ".join(f"{k} = '{v}'" for k, v in where.items())
        query += f" WHERE id = {id}"
        # тут могут быть ошибки, если пользователь ввел не существующие колонки
        cur.execute(query) 
        

def delete_from_file(file_name, **kwargs):
    with sq.connect(file_name) as file:
        cur = file.cursor()
        query = "DELETE FROM people WHERE " + " AND ".join(f"{k} = '{v}'" for k, v in kwargs.items())
        # тут могут быть ошибки, если пользователь ввел не существующие колонки
        cur.execute(query)


COLUMNS_NAME = ['id', 'name', 'country', 'age']
FILE_NAME = "task_49.db"
people = [{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, 
 {"name": "Matthew King", "country": "Colombia", "age": 34}, 
 {"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, 
 {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, 
 {"name": "Sarah Contreras", "country": "Honduras", "age": 82}, 
 {"name": "Danielle Williams", "country": "Togo", "age": 91}, 
 {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, 
 {"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, 
 {"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, 
 {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, 
 {"name": "Christina Fernandez", "country": "Burundi", "age": 71}, 
 {"name": "Allen Norton", "country": "Montserrat", "age": 79}, 
 {"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, 
 {"name": "Brooke Boyd", "country": "Latvia", "age": 74}, 
 {"name": "Jerry Morrow", "country": "San Marino", "age": 23}, 
 {"name": "Danielle Bradshaw", "country": "Vietnam", "age": 64}, 
 {"name": "Jerry Thompson", "country": "Belgium", "age": 30}, 
 {"name": "Mark Jordan", "country": "Comoros", "age": 89}, 
 {"name": "Joseph Berger", "country": "Cook Islands", "age": 94}, 
 {"name": "Gina Brooks", "country": "Samoa", "age": 51}, 
 {"name": "Walter Duran", "country": "Chad", "age": 67}, 
 {"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, 
 {"name": "Johnny Glover", "country": "Eritrea", "age": 72}, 
 {"name": "Lindsay Moore", "country": "Liberia", "age": 53}, 
 {"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, 
 {"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, 
 {"name": "Charles Thompson", "country": "Saudi Arabia", "age": 50}, 
 {"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, 
 {"name": "David Decker", "country": "South Africa", "age": 71}, 
 {"name": "Christopher Perez", "country": "Cayman Islands", "age": 49},
 {"name": "Debra Hall", "country": "Greece", "age": 13}, 
 {"name": "John King", "country": "Bahamas", "age": 40}, 
 {"name": "Justin Galvan", "country": "Namibia", "age": 19}, 
 {"name": "Jacqueline Berger", "country": "Yemen", "age": 59}, 
 {"name": "Shawn Robinson", "country": "Saint Pierre and Miquelon", "age": 32}, 
 {"name": "Kristen Garcia", "country": "Portugal", "age": 48}, 
 {"name": "Christopher Barry", "country": "French Polynesia", "age": 23}, 
 {"name": "Alejandra Cook", "country": "Egypt", "age": 16}, 
 {"name": "Jill Harrell", "country": "Comoros", "age": 49}, 
 {"name": "Sara Zimmerman", "country": "Brazil", "age": 26}, 
 {"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75},
 {"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, 
 {"name": "Larry Wong", "country": "New Caledonia", "age": 6}, 
 {"name": "Brenda Acosta", "country": "Grenada", "age": 48}, 
 {"name": "Latoya Terry", "country": "Saint Martin", "age": 41}, 
 {"name": "Seth Luna", "country": "Sao Tome and Principe", "age": 59}, 
 {"name": "Micheal Adams", "country": "Barbados", "age": 53}, 
 {"name": "Susan Carroll", "country": "Somalia", "age": 64}, 
 {"name": "Douglas Morris", "country": "Thailand", "age": 24}, 
 {"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, 
 {"name": "Kristin Johnson", "country": "Niue", "age": 71}, 
 {"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, 
 {"name": "Jared Smith", "country": "Colombia", "age": 46}, 
 {"name": "Lauren Anderson", "country": "Christmas Island", "age": 46}, 
 {"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, 
 {"name": "Maria Edwards", "country": "Hungary", "age": 78}, 
 {"name": "Anne Lee", "country": "United States of America", "age": 10}, 
 {"name": "James Mckenzie", "country": "Uganda", "age": 43}, 
 {"name": "Joshua Gallegos", "country": "United States Minor Outlying Islands", "age": 27}, 
 {"name": "Paul Herrera", "country": "Kiribati", "age": 17}, 
 {"name": "Veronica White", "country": "Gabon", "age": 88}, 
 {"name": "Michael Hall", "country": "China", "age": 43}, 
 {"name": "Sabrina Thompson", "country": "Chad", "age": 27}, 
 {"name": "Jennifer Archer", "country": "Korea", "age": 45}, 
 {"name": "Christina Simmons", "country": "Israel", "age": 80}, 
 {"name": "Travis White", "country": "Central African Republic", "age": 31}, 
 {"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, 
 {"name": "Matthew Richards", "country": "Svalbard & Jan Mayen Islands", "age": 34}, 
 {"name": "Stephen Curry", "country": "Finland", "age": 92}, 
 {"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, 
 {"name": "Mary Estes", "country": "Montenegro", "age": 19}, 
 {"name": "Alex Scott", "country": "Christmas Island", "age": 67}, 
 {"name": "John Andrews", "country": "Bahamas", "age": 68}, 
 {"name": "Jonathan Willis", "country": "Saint Martin", "age": 23}, 
 {"name": "Olivia Campos", "country": "Armenia", "age": 72}, 
 {"name": "Diana Davis", "country": "Azerbaijan", "age": 54}, 
 {"name": "Jack Cummings", "country": "Martinique", "age": 94}, 
 {"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, 
 {"name": "Maria Blake", "country": "Pitcairn Islands", "age": 91}, 
 {"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, 
 {"name": "John Terrell Jr.", "country": "India", "age": 50}, 
 {"name": "Lindsay Wood", "country": "United Arab Emirates", "age": 72}, 
 {"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, 
 {"name": "Tanner Johnson", "country": "Congo", "age": 11}, 
 {"name": "Michael Garcia", "country": "Liberia", "age": 45}, 
 {"name": "Nicole Johnson", "country": "Barbados", "age": 54}, 
 {"name": "William Lee", "country": "Lithuania", "age": 59}, 
 {"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, 
 {"name": "Sandra Freeman", "country": "Philippines", "age": 35}, 
 {"name": "Latoya Maxwell", "country": "Sweden", "age": 12}, 
 {"name": "Darius Blevins", "country": "Thailand", "age": 29}, 
 {"name": "Teresa Newman", "country": "Jersey", "age": 6}, 
 {"name": "Larry Bray", "country": "Brunei Darussalam", "age": 21}, 
 {"name": "Adam Roberson", "country": "Jordan", "age": 71}, 
 {"name": "Michael Gomez", "country": "Tajikistan", "age": 37}, 
 {"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, 
 {"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, 
 {"name": "Kevin Wagner", "country": "Suriname", "age": 55}, 
 {"name": "Peggy Bryant", "country": "Korea", "age": 36}, 
 {"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]


drop_table_in_file(FILE_NAME)
create_db(FILE_NAME)
write_in_file(FILE_NAME, people)
pprint(read_from_file(FILE_NAME))
# pprint(read_from_file(FILE_NAME, age = 66))
# update_from_file_by_id(FILE_NAME, 67, country = "Namibia")
# pprint(read_from_file(FILE_NAME, age = 67))
# delete_from_file(FILE_NAME, id = 67)
# pprint(read_from_file(FILE_NAME, age = 67))
