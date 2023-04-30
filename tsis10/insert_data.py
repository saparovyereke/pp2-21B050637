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

r = input("Choose how you will insert data 1 from csv file , or 2 friom terminal\nType 1 if csv file ,type 2 if second method\n")

if r == '1':
	f = open("info.csv", "r")
	cursor.copy_from(f, 'phonebook', sep=',')
	f.close()
	print("successfully !!");
else:
	cnt=0
	first_name = str(input("First name: "))
	num = int(input("Num: "))
	sql = f"select * from phonebook";
	cursor.execute(sql)
	info = cursor.fetchall()
	for i in range(len(info)):
		if info[i][0]==first_name:
			cnt+=1
	if cnt==0:
		postgres_insert_query = """ INSERT INTO  phonebook(first_name,phone_num) VALUES (%s,%s)"""
		record_to_insert = (first_name, num)
		cursor.execute(postgres_insert_query, record_to_insert)
		print("successfully !!");
	else:
		print("User with this name already exist!")

conn.commit()

conn.close()