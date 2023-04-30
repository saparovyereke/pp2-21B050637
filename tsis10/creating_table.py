import psycopg2

conn = psycopg2.connect(
  database="phonebook",
  user='lab10_user',
  password='zhasik04',
  host='localhost',
  port= '5432'
)

conn.autocommit = True

cursor = conn.cursor()

"""
query to create a database
sql = ''' CREATE database phonebook ''';

create user
sql = ''' CREATE ROLE lab10_user WITH PASSWORD 'zhasik04' LOGIN''';
"""

#create table
sql = '''CREATE TABLE phonebook(
  first_name VARCHAR(255) NOT NULL,
  phone_num VARCHAR(255)
)''';

cursor.execute(sql)
print("Database has been created successfully !!");

conn.close()