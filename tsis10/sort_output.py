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

"""
output all users
sql = f"select * from phonebook";

ouptup exact user
sql = f"select * from phonebook where first_name = \'zhasikaset\' ";

output by sorted names(decrease)
sql = f"select * from phonebook by order by first_name desc";
"""

#output by sorted names(increase)
sql = f"select * from phonebook by order by first_name asc";

cursor.execute(sql)
info = cursor.fetchall()
print(info)