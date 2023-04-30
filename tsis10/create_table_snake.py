import psycopg2

conn = psycopg2.connect(
  database="snake_game",
  user='lab10_user',
  password='zhasik04',
  host='localhost',
  port= '5432'
)

conn.autocommit = True

cursor = conn.cursor()

#create table
sql = '''CREATE TABLE snake_game(
  user_name VARCHAR(255) NOT NULL,
  last_score INT,
  max_score INT
)''';

cursor.execute(sql)
print("Database has been created successfully !!");

conn.close()