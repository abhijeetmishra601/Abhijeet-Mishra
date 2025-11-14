print("Hello world")
if 5 > 2:
    print("5 is greater than 2")

x = 5
y = 3
print(x + y)
print(x * y)
print(x / y)
print(x - y)

print("this is python")

x = 13
y = "neeraj"
print(x)
print(y)

x = 4.5
print(type(x))

x = 4
y = 5
print(bool(x + y))
print(bool(x))

x = ""
print(bool(x))
x = "5"
print(bool(x))

my_var = 40
print(my_var)

x, y, z = "30", "40", "50"
print(x)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(type(x))

fruits = [2, 4, 7, 4, 6, 8, 9, 10]
print(fruits)
print(type(fruits))

x = "python"
y = "is"
z = "good"
print(x, y, z)
print(x + y + z)

def my_func():
    print("python is " + x)

my_list = ["apple", "banana", 1, 3, 5, 7]
my_list[2:5] = ["abc"]
print(my_list)

text = "hello"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("hello", "world"))
print(text.split())

x = "abc"
y = 15
print(f"my name is {x} and my age is {y}")

x = 10
x -= 3
print(x)

x = 5
y = 10
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)
print(x < y)

x = 10
print(x > 3 and x < 11)
print(not (x > 3))

x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)

colors = {"red", "green", "blue"}
print(colors)
colors.add("yellow")
print(colors)
colors.remove("green")
for color in colors:
    print(color)

students = {"name": "abc", "age": 18, "grade": "a"}
print(students)
print(students["name"])
print(students.get("age"))

age = 20
if age >= 18:
    print("you are adult")
else:
    print("you are not adult")

list1 = [1, 2, 3, 4, 5, 6]
list1.insert(2, "apple")
print(list1)
list1.append("banana")
print(list1)
list1.remove("apple")
print(list1)
list1.pop()
print(list1)
list1.clear()
print(list1)

list1 = []
list1.append(1)
print(list1)

list1[0] = "hello"
print(list1)

list1 = [1, 2, 3, 4, 4, 4, 5]
for x in list1:
    print(x)

age = 20
if age >= 18:
    print("you are adult")
elif age == 18:
    print("you are teen")
elif age == 17:
    print("you are 17")
elif age == 16:
    print("you are 16")
else:
    print("you are not adult")

x = 15
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is not greater than 20")

x = 15
if x % 2 == 0:
    print("even")
else:
    print("odd")

word = "python"
for x in word:
    print(x)

for i in range(9):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

def greet(name):
    print(f"hello, {name}")

greet("alice")
greet("bob")

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

def greet(name="student"):
    print(f"hello, {name}")

greet()
greet("abhijeet")

x = 12
def my_func():
    y = 5
    print(x, y)

my_func()
print(x)

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving")

car1 = Car("BMW", "black")
car1.drive()

import array
number = array.array('i', [1, 2, 3, 4, 5])
print(number)

from numpy import random

x = random.randint(100)
print(x)

x = random.rand()
print(x)

x = random.randint(100, size=(3, 5))
print(x)

x = random.randint(100, size=(2, 3, 5))
print(x)

x = random.randint(100, size=(2, 2, 3, 5))
print(x)

import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)
