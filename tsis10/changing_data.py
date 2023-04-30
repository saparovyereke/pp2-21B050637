import psycopg2

conn = psycopg2.connect(
  database="phonebook",
  user='lab10_user',
  password='zhasik04',
  host='localhost',
  port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True

old_name = str(input("First_old: "))
num_old = int(input("Num_old: "))
sql = f"select * from phonebook where first_name =\'{old_name}\' and phone_num = \'{num_old}\' "
cursor.execute(sql)
info = cursor.fetchall()

if len(info) > 0:
  new_name = str(input("First_new: "))
  new_phone = int(input("Num_new: "))
  sql_update = f"Update phonebook set phone_num =\'{new_phone}\', first_name =\'{new_name}\' where first_name =\'{old_name}\' ; " 
  cursor.execute(sql_update)
  print("successfully !!");
else:
  print("this people name is not in phonebook")


conn.commit()

conn.close()