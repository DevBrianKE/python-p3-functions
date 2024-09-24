#!/usr/bin/env python3

# Function 1: greet_programmer
def greet_programmer():
    print("Hello, programmer!")

# Function 2: greet
def greet(name):
    print(f"Hello, {name}!")

# Function 3: greet_with_default
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Function 4: add
def add(num1, num2):
    return num1 + num2

# Function 5: halve
def halve(number):
    if not isinstance(number, (int, float)):  # Check if number is not int or float
        return None
    return number / 2
