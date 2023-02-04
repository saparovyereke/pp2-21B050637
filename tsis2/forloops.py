fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#looping through string
for x in "banana":
  print(x)

#break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

#continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range() function
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

#increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
  print(x)

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!") 

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") 

#Nested loop is loop inside the loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 

#pass statement
for x in [0, 1, 2]:
  pass

#exercises
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)