a = 33
b = 200
if b > a:
  print("b is greater than a")



a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short Hand If
if a > b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B") 


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 

#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")



#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 


#pass statement

a = 33
b = 200

if b > a:
  pass

#exercises
a = 50
b = 10
if a > b:
  print("Hello World")

a = 50
b = 10
if a != b:
  print("Hello World")

a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

a = 50
b = 10
if a == b:
  print("1")
elif a>b:
  print("2")
else:
  print("3")

if a == b and c == d:
  print("Hello")

if a == b or c == d:
  print("Hello")

if 5 > 2:
 print("Five is greater than two!")

if 5 > 2: print("Five is greater than two!")

print("Yes") if 5 > 2 else print("No")