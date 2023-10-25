import subprocess
# subprocess.call(['sh', './test.sh'])


print ("Hello, world!")

# https://www.w3schools.com/python/default.asp

x = 5

if x > 2:
    print(x, "is greater than two")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = "a snake"

def myfunc():
  print("Python is " + x)

myfunc()

b = "Hello, World!"
print(b[2:5])
print(b[2:])
print(b.upper())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c)

age = 36
txt = "My name is John, and I am {}, seriously, {}"
print(txt.format(age, age))
txt = "We are the so-called \"Vikings\" from the north."

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(""))
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print(bool(15))

def myFunction() :
  return True if a == 200 else False

def myFunction() :
  if a == 200 and not a == 201:
    return True 
  else:
    return False
  
def myFunction() :
    if a == 200 & a != 201:
        return True 
    else:
        return False

print(myFunction())

x = 3
x //= 2
print(x ** 2) if x is 2 else print(x | 0)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:5] = ["blackcurrant", "watermelon"]                          #[index to insert from:index to insert to]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x, "\n")

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

mylist = ["apple", "banana", "cherry"]
x = len(mylist)
print(x)

# https://miro.medium.com/v2/resize:fit:1134/1*WMiNIQ9THariDSJw47uU1w.png

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

for x in "banana":
    print(x)

def my_function():
  print("Hello from a function")


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")  # If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. 
                                        # This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

x = lambda a : a + 10
print(x(1))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

# del p1.x
# print(p1.x)

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

def myfunc():
  global x
  x = 300

myfunc()

print(x)

import module
module.greeting("Tom")
a = module.person1["age"]
print(a)

import module as mx
a = mx.person1["age"]
print(a)

import platform

x = platform.system()
print(x)
x = dir(platform)
print(x)

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) # https://www.w3schools.com/python/python_datetime.asp

# x = dir(datetime.datetime)
# print(x)

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)

import math

x = math.sqrt(64)

print(x)

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(len(x))

import os
os.system('pip --version')
# os.system('test.sh')

# username = input("Enter username: ")
# print("Username is: " + username)

s1 = 'A'
s2 = '1'
# first numbers, then letters, lexicographic ordering comparison

if s1 > s2:
  print("A > 1")

# "is" = referenz, ""=="" = wert
