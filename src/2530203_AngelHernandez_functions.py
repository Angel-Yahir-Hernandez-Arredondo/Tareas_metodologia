"""
Function Management in Python
Angel Yahir Hernandez Arredondo
2530203
IM 1-3
"""

# Executive Summary
# This document explains the fundamentals of function handling in Python.
# Functions fulfill different purposes, such as using "def" to define a function
# and "return" to send a value back to the caller.
# It also covers default parameters, arguments, and how functions help organize
# code into reusable and structured components.

# Principles and Best Practices
# It is recommended to create small functions that perform a single task 
# (single responsibility), which makes them easier to understand, test, 
# and reuse.
# Avoid repeating code: if you notice that you copy and paste logic, it is
# better to extract it into a separate function.
# Whenever possible, try to keep functions “pure”; meaning that the same input
# always produces the same output and they do not depend on external variables.
# Document each function with simple comments explaining what it does and 
# what parameters it receives.
# Use clear and descriptive names for your functions 
# (for example, calculate_bmi instead of f1 or do_it).


#7.3 Problem 1: Rectangle area and perimeter (basic functions)
#Define two functions to calculate the area and perimeter of a rectangle.
#The functions should take the width and height of the rectangle as parameters

# Inputs:
# - width (float)
# - height (float)
# Outputs:
# - "Area" (value)
# - "Perimeter" (value)

#validations:
# - width and height must be positive numbers

# Test cases:
# 1) Normal:
#    Input: width=5, height=3
#    Expected: Area=15, Perimeter=16
#
# 2) Border:
#    Input: width=0.01, height=0.01
#    Expected: Area=0.0001, Perimeter=0.04
#
# 3) Error:
#    Input: width=-4, height=2
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def calculate_area(width, height):
    """Returns the area of a rectangle."""
    return width * height


def calculate_perimeter(width, height):
    """Returns the perimeter of a rectangle."""
    return 2 * (width + height)



width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))    

if width > 0 and height > 0:
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    print("Area:", area)
    print("Perimeter:", perimeter)
else:
    print("Error: invalid input")


#7.3 Problem 2: Grade classifier (functions with return string)
# ----------------------------------------------------
# Description:
#   This program defines a function that receives a
#   numeric grade (0–100) and returns a letter category
#   according to standard grading ranges.
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - 0 <= score <= 100
# - If invalid, print "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: score=85
#    Expected: Category="B"
#
# 2) Border:
#    Input: score=90
#    Expected: Category="A"
#
# 3) Error:
#    Input: score=150
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def classify_grade(score):
    """Returns a letter grade based on the numeric score."""
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"



score = float(input("Enter the score: "))

if 0 <= score <= 100:
    category = classify_grade(score)
    print("Score:", score)
    print("Category:", category)
else:
    print("Error: invalid input")


# =========================================================
# 7.3 Problem 3: List Statistics Function (min, max, average)
# =========================================================
# INPUT:
#   - A list of numbers entered by the user, separated by commas.
#
# OUTPUT:
#   - A dictionary with {"min": ..., "max": ..., "average": ...}
#
# VALIDATIONS:
#   - Empty input
#   - Number conversion errors
#   - Non-empty final list
#
# TESTING:

# 1. Valid case (normal operation)
# Input: [4, 8, 12]
# Expected output:
# {"min": 4, "max": 12, "average": 8}

# 2. Edge case (only one number)
# Input: [7]
# Expected output:
# {"min": 7, "max": 7, "average": 7}

# 3. Invalid case (contains a non-numeric value)
# Input: "10, 5, hello, 3"
# Expected output:
# Error: invalid number detected ("hello")



def summarize_numbers(numbers_list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {"min": min_value, "max": max_value, "average": average_value}


numbers_text = input("Ingresa números separados por comas: ").strip()

if numbers_text == "":
    print("Error: input vacío")
else:
    try:
        numbers_list = [float(x) for x in numbers_text.split(",")]

        if len(numbers_list) == 0:
            print("Error: lista vacía")
        else:
            stats = summarize_numbers(numbers_list)
            print("---- RESULTADOS ----")
            print("Min:", stats["min"])
            print("Max:", stats["max"])
            print("Average:", stats["average"])

    except ValueError:
        print("Error: input no numérico")


# =========================================================
# 7.4 Problem 4: Apply Discount to List (Pure Function)
# =========================================================
# INPUT:
#   - A list of prices entered by the user, separated by commas
#   - A discount rate between 0 and 1
#
# OUTPUT:
#   - A new list containing the discounted prices
#
# VALIDATIONS:
#   - Empty list
#   - Negative prices
#   - Invalid discount rate
# TESTING:
# 1. Valid case (normal operation)
# Input: prices=[100, 200, 300], discount_rate=0.1
# Expected output:
# Discounted prices: [90.0, 180.0, 270.0]       
# 2. Edge case (zero discount)
# Input: prices=[50, 75, 100], discount_rate=0.0
# Expected output:
# Discounted prices: [50.0, 75.0, 100.0
# 3. Invalid case (negative price)
# Input: prices=[20, -5, 30], discount_rate=0.2
# Expected output:
# Error: prices must be greater than 0

def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]


prices_text = input("Ingresa precios separados por comas: ").strip()

try:
    discount_rate = float(input("Ingresa la tasa de descuento (0 a 1): "))
except ValueError:
    print("Error: la tasa debe ser numérica")
    discount_rate = -1  # Forzar error

if prices_text == "" or not (0 <= discount_rate <= 1):
    print("Error: input inválido")
else:
    try:
        prices_list = [float(p) for p in prices_text.split(",")]

        if any(p < 0 for p in prices_list):
            print("Error: los precios deben ser mayores que 0")
        else:
            discounted_list = apply_discount(prices_list, discount_rate)

            print("---- RESULTADOS ----")
            print("Original prices:", prices_list)
            print("Discounted prices:", discounted_list)

    except ValueError:
        print("Error: input no numérico")


# =========================================================
# 7.5 Problem 5: Greeting Function (Default Parameters)
# =========================================================
# INPUT:
#   - Name and an optional title
#
# OUTPUT:
#   - A formatted greeting string
#
# TESTING:
# 1. Valid case (name only)
# Input: name="Alice"
# Expected output:  
# Hello, Alice!
# 2. Edge case (name with extra spaces)
# Input: name="  Charlie  ", title="Eng."
# Expected output:
# Hello, Eng. Charlie!
# 3. Valid case (name with title)
# Input: name="Bob", title="Dr."   
# Expected output:
# Hello, Dr. Bob!


def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name
    return f"Hello, {full_name}!"

print(greet("Alice"))
print(greet("Bob", "Dr."))
print(greet(name="Charlie", title="Eng."))

# ----------------------------------------------------
# Problem 6: Factorial function (iterative or recursive)
# Description:
#   This program defines a function factorial(n) that
#   returns the factorial of a non-negative integer n.
#   The implementation used here is iterative, because
#   it avoids recursion depth limits and is easier to
#   understand for large values of n.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be an integer
# - n >= 0
# - Optional: n <= 20 to avoid extremely large numbers
# - If validation fails, print "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: n=5
#    Expected: Factorial=120
#
# 2) Border:
#    Input: n=0
#    Expected: Factorial=1
#
# 3) Error:
#    Input: n=-3
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def factorial(n):
    """Returns n! using an iterative approach."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ---- Main program ----

# Ask user for input
user_input = input("Enter a non-negative integer: ")

# Validate that input is an integer
if user_input.isdigit():  # ensures digits only, no negatives
    n = int(user_input)

    # Validate range
    if 0 <= n <= 20:
        fact_value = factorial(n)
        print("n:", n)
        print("Factorial:", fact_value)
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")

# Conclusion
"""
In these exercises, I was able to apply and better understand several key 
programming methods and concepts. I used user-defined functions to organize 
the code into specific tasks, such as calculate_area(), classify_grade(), 
summarize_numbers(), apply_discount(), and factorial(). I also worked with 
Python's built-in methods such as min(), max(), sum(), and list comprehensions, 
which allow data to be processed more efficiently. Additionally, I reinforced 
input validation using methods like .isdigit() and improved error handling 
through try-except blocks.

Overall, these methods helped me structure cleaner, safer, and more functional 
programs, which is essential for developing reliable solutions in mechatronics 
applications.
"""

# References
# https://ellibrodepython.com/funciones-en-python
# https://www.datacamp.com/es/tutorial/functions-python-tutorial
# https://ebac.mx/blog/funciones-de-python
# https://aprendeconalf.es/docencia/python/manual/funciones/
# https://aulavirtual.espol.edu.ec/courses/4558/pages/funciones-en-python