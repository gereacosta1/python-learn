#https://www.youtube.com/watch?v=K5KVEU3aaeQ&t=3541s
# pyhon run es con el comando ctrl + r

name = input("What is your name? ")
print(f"Hello, {name}!")


#Basic of variables
students_count = 1000
rating = 4.99
is_published = True
course = "Python Programming for Beginners"

print(f"Course: {course}, Students Count: {students_count}, Rating: {rating}, Published: {is_published}")

#strings
couser = "Python Programming for Beginners"
message = """
Welcome to the course!
This course will teach you the basics of Python programming.
Make sure to complete all the exercises and projects.
"""

print(len(couser))  # Length of the string
print(couser[0])  # First character
print(couser[0:6])  # Slicing the string



first = "John"
last = "Doe"
full = f"{first} {last}"
print(full)  # Formatted string



course = "Python Programming for Beginners"
print(course.upper())  # Convert to uppercase
print(course.lower())   # Convert to lowercase
print(course.find("Programming"))  # Find substring
print(course.replace("Beginners", "Advanced"))  # Replace substring
print("Python" in course)  # Check if substring exists
print(course.strip())  # Remove whitespace
print("pro" in course())  # Check if 'pro' is in the course string 
print("switch" not in course)  # Check if 'switch' is not in the course string

X = 1
X = 2.1
X = 1 + 2J

print(2 + 2)  # Addition
print(2 - 2)  # Subtraction
print(2 * 2)    # Multiplication
print(2 / 2)    # Division
print(2 ** 3)   # Exponentiation
print(10 // 3)  # Floor division
print(10 % 3)   # Modulus
print(abs(-2))  # Absolute value
print(round(2.9))  # Round to nearest integer



#working with numbers
print(round(2.9))  # Round to nearest integer
print(abs(-2.9))  # Absolute value

import math

math.ceil(2.9)  # Round up
math.floor(2.9)  # Round down
print(math.pi)  # Value of pi
print(math.e)  # Value of e

