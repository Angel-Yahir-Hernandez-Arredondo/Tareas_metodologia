"""
Student: Angel Yahir Hernandez Arredondo
ID: 2530203
Group: 1-3
Assignment: Fibonacci Series Generator in Pytho
EXECUTIVE SUMMARY
The Fibonacci series is a sequence where each term is obtained by adding 
the previous two numbers, starting from 0 and 1. This program reads an 
integer n from the user and generates the first n Fibonacci terms. It 
includes input validation to ensure n is a valid integer and n >= 1. A 
loop is used to iteratively compute the sequence. The objective is to 
practice loops, validation, and formatted output in Python
PROBLEM: FIBONACCI SERIES GENERATOR
Description:
Program that reads an integer n and prints the first n terms of the 
Fibonacci series, starting from 0 and 1.

Inputs:
- n (int; number of terms to generate)

Outputs:
- "Fibonacci series:" followed by the n terms separated by spaces"""
"""
Test cases:

1) Normal case:
   Input: number = 7
   Expected output:
   Fibonacci series: 0, 1, 1, 2, 3, 5, 8

2) Border case:
   Input: number = 1
   Expected output:
   Fibonacci series: 0

3) Error case:
   Input: number = "abc"   (non-numeric)
   Expected output:
   error:invalid input

"""
number= input("Set your numbers term: ")

if not number.isdigit():
    print("Error: invalid input")
    exit()

n = int(number)

if n<1 or n>50:
    print("Number is not in the range")
    exit()
elif n==1:
    print("Fibonacci: 0")
    exit()
elif n==2:
    print("Fibonacci: 0, 1")
    exit()

fibo=[0,1]

for i in range(2, n):
    next_term=fibo[i-1]+fibo[i-2]
    fibo.append(next_term)

fibo_text=", ".join(str(x) for x in fibo)

print(f"Fibonacci: {fibo_text}")
"""
CONCLUSIONS
Using a loop made it possible to build the Fibonacci sequence step by step 
without needing complex formulas. Handling special cases such as n = 1 or 
n = 2 ensures the program behaves correctly for all valid inputs. The logic 
for generating Fibonacci numbers can be reused in other programs that 
require iterative sequences or cumulative calculations.

REFERENCES
Python Official Documentation – Built-in Types (List, Tuple, Dict)
https://docs.python.org/3/library/stdtypes.html

Python Official Tutorial – Input & Output
https://docs.python.org/3/tutorial/inputoutput.html

W3Schools – Python Lists
https://www.w3schools.com/python/python_lists.asp

Real Python – Handling Errors With Exceptions
https://realpython.com/python-exceptions/

GeeksforGeeks – Python Program to Check Valid Strings / isalpha()
https://www.geeksforgeeks.org/python-string-isalpha-application/
"""

# URL repository:
# https://github.com/Angel-Yahir-Hernandez-Arredondo/Tareas_metodologia.git