import psycopg2

conn = psycopg2.connect(
  database="phonebook",
  user='lab10_user',
  password='zhasik04',
  host='localhost',
  port='5432'
)
cursor = conn.cursor()
conn.autocommit = True

first_old = str(input("First_old: "))

sql = f"select * from phonebook where first_name =\'{first_old}\'"
cursor.execute(sql)
info = cursor.fetchall()

if len(info) > 0:
  sql_update = f"Delete from phonebook where  first_name =\'{first_old}\'; " 
  cursor.execute(sql_update)
  print("successfully !!");
else:
  print("this people name is not in phonebook")

conn.commit()

conn.close()