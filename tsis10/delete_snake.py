import psycopg2

conn = psycopg2.connect(
  database="snake_game",
  user='lab10_user',
  password='zhasik04',
  host='localhost',
  port='5432'
)
cursor = conn.cursor()
conn.autocommit = True

user_name = str(input("user_name: "))

sql = f"select * from snake_game where user_name =\'{user_name}\'"
cursor.execute(sql)
info = cursor.fetchall()

if len(info) > 0:
  sql_update = f"Delete from snake_game where  user_name =\'{user_name}\'; " 
  cursor.execute(sql_update)
  print("successfully !!");
else:
  print("this people name is not in snake_game")

conn.commit()

conn.close()