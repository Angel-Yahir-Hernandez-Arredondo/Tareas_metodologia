# Name: Angel Yahir Hernandez Arredondo
# Student ID: 2530203
# Group: 1-3


# EXECUTIVE SUMMARY
# In Python, integers (int) represent whole numbers, while floats represent
# numbers with decimals. Booleans (True/False) are logical values produced
# mainly from comparisons and conditional expressions. Validating numerical
# ranges is essential to prevent runtime errors, including division by zero,
# negative values where not allowed, or impossible physical conditions.
# This document includes six problems using ints, floats, and booleans to
# perform arithmetic, comparisons, logical evaluations, decisions, and data
# validation. Each problem contains a description, inputs, outputs, and
# validations following the project's specifications.

# PRINCIPLES AND BEST PRACTICES
# - Use appropriate data types: int for counters, float for decimal values.
# - Avoid repeating complex expressions: store intermediate results in variables.
# - Validate all user inputs before operating (non-negative values, correct ranges).
# - Use descriptive variable names and clear output messages for the user.
# - Document the meaning of boolean values in each context so the program is easy
#   to interpret and maintain.
"""
PROBLEM 1: Temperature converter and range flag
Description:
Converts a temperature in Celsius to Fahrenheit and Kelvin. Also determines
a boolean flag indicating whether the Celsius temperature is high (>= 30.0).
Inputs:
temp_c (float)
Outputs:
"Fahrenheit:" <temp_f>
"Kelvin:" <temp_k>
"High temperature:" true|false
Validations:
temp_c must be convertible to float.
Kelvin temperature must not be physically impossible (>= 0.0).
Test cases:

Normal
Input: 25
Salida:
Fahrenheit: 77.0
Kelvin: 298.15
High temperature: False

Border (30°C)
Input: 30
Salida:
Fahrenheit: 86.0
Kelvin: 303.15
High temperature: True

Error
Input: -300
Salida:
Error: invalid input

"""
# (CODE HERE)

temp = input("set your temperature in celsius\n")
high_temp=False
try:
    celcious=float(temp)
    if celcious >-273.15:
        fahrenheit = (celcious*9/5)+32
        kelvin = celcious+273.15
        print(f"fahrenheit: {fahrenheit}")
        print(f"kelvin: {kelvin}")
        if celcious>= 30:
            high_temp=True
        
        print(f"high temperature: {high_temp}")
    else:
        print("Error:invalid input")
    
except ValueError:
    print("error : invalid input")
    
"""

PROBLEM 2: Work hours and overtime payment
Description:
Calculates total weekly payment including overtime at 150% of the hourly rate
when hours worked exceed 40. Determines a boolean indicating overtime.
Inputs:
hours_worked (float)
hourly_rate (float)
Outputs:
"Regular pay:" <regular_pay>
"Overtime pay:" <overtime_pay>
"Total pay:" <total_pay>
"Has overtime:" true|false
Validations:
hours_worked >= 0
hourly_rate > 0
If not satisfied, print "Error: invalid input".

test cases

Normal
Input: hours=45, rate=100
Salida:
Regular pay: 4000.0
Overtime pay: 750.0
Total pay: 4750.0
Has overtime: True

Border (40 horas)
Input: hours=40, rate=120
Salida:
Regular pay: 4800.0
Overtime pay: 0.0
Total pay: 4800.0
Has overtime: False

Error
Input: hours=-5, rate=100
Salida:
Error: invalid input
"""

# (CODE HERE)

hours_worked = input("please set your worked hours\n")
hourly_rate = input("please set your hourly rate\n")
valid =False
has_overtime = False
overtime_payment=0
try:
   pay= float(hourly_rate)
   time= float (hours_worked)
   valid =True
    
except ValueError:
    print ("you have an invalid input either in hourly rate or hours worked")

if valid==True: 
    if pay <= 0 or time<0:
        print("Error:invalid input") 
    elif time>40:
        regular_payment= 40*pay 
        overtime_payment = (time-40)*(pay*1.5)  
        total_payment = regular_payment + overtime_payment 
        has_overtime=True
        print(f"regular pay : {regular_payment}")
        print(f"overtime pay : {overtime_payment}")
        print(f"your payment is {total_payment}")
        print(f"has overtime:{has_overtime}")
    else:
        total_payment = time* pay 
        print(f"your total payment is : ")
        print(f"regular pay : {total_payment}")
        print(f"overtime pay : {overtime_payment}")
        print(f"your payment is : {total_payment}")
        print(f"has overtime:{has_overtime}")

"""
PROBLEM 3: Discount eligibility with booleans
Description:
Determines if a customer is eligible for a discount based on student status,
senior status, or purchase total. Applies a 10% discount when eligible.
Inputs:
purchase_total (float)
is_student_text ("YES" or "NO")
is_senior_text ("YES" or "NO")
Outputs:
"Discount eligible:" true|false
"Final total:" <final_total>
Validations:
purchase_total >= 0.0
is_student_text and is_senior_text must be "YES" or "NO"
Otherwise print "Error: invalid input".

test cases

Normal
Input: purchase_total=1500, student=NO, senior=NO
Salida:
Discount eligible: True
Final total: 1350.0

Border
Input: purchase_total=1000, student=NO, senior=NO
Salida:
Discount eligible: True
Final total: 900.0

Error
Input: purchase_total=500, student=MAYBE, senior=NO
Salida:
Error: invalid input

"""

# (CODE HERE)

print ("welcome to the discount elegibility system")
purchase_total= input("set your total purchase\n")
is_student=input("are you a student\n YES/NO\n").upper() 
is_senior= input("are you a senior citizen\n YES/NO\n").upper()
valid=False 
student_conf=False
senior_conf=False   
affirmations =["YES","NO"] 
try:
  purchase = float(purchase_total)
  if purchase >= 0.0: 
    valid =True
except ValueError:
  print("please set a valid total")
for i in affirmations:
  if is_student == i:
    student_conf=True 
  if is_senior== i:
    senior_conf=True 
if valid and student_conf and senior_conf:
    if is_student=="YES" or is_senior=="YES" or purchase>=1000.0:
      discount=True
    else:
      discount=False
    print(f"Discount elegible : {discount}")
    if discount:
        print(f"final total: {purchase*.9}")
    else:
        print(f"final total: {purchase}")
else:
  print("error:invalid input")

"""
PROBLEM 4: Basic statistics of three integers
Description:
Reads three integers and calculates sum, average, maximum, minimum, and a
boolean indicating whether all three numbers are even.
Inputs:
n1 (int)
n2 (int)
n3 (int)
Outputs:
"Sum:" <sum_value>
"Average:" <average_value>
"Max:" <max_value>
"Min:" <min_value>
"All even:" true|false
Validations:
All three values must be convertible to int.

test cases

Normal
Input: 4, 8, 12
Salida:
Sum: 24
Average: 8.0
Max: 12
Min: 4
All even: True

Border (número impar mezclado)
Input: 2, 3, 6
Salida:
Sum: 11
Average: 3.6666666666666665
Max: 6
Min: 2
All even: False

Error
Input: 3, abc, 5
Salida:
Error: invalid number
"""

# (CODE HERE)

print("welcome to the statistics calculator")
numbers=[]
counter=0
while True:
    num1 = input("please set your first \n")
    num2 = input("please set your second \n")
    num3 = input("please set your third \n")
    try:
        nat1= int(num1)
        nat2= int(num2)
        nat3= int(num3)
        numbers.extend([nat1,nat2,nat3])
        break 
    except ValueError:
        print("error:invalid number")
for number in numbers:
    if number%2==0:
        counter=counter+1
print(f"sum:{sum(numbers)}")
print(f"average:{(sum(numbers))/3}")
print(f"maximum value:{max(numbers)}")
print(f"minimum value: {min(numbers)}")
print(f"all even: {counter==3}")

"""
PROBLEM 5: Loan eligibility (income and debt ratio)
Description:
Determines whether a person qualifies for a loan based on income, debt ratio,
and credit score.
Inputs:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
Outputs:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false
Validations:
- monthly_income > 0.0
- monthly_debt >= 0.0
- credit_score >= 0
- Otherwise print "Error: invalid input".

test cases

Normal
Input: income=9000, debt=2000, score=700
Salida:
Debt ratio: 0.22
Eligible: True

Border
Input: income=8000, debt=3200, score=650
Salida:
Debt ratio: 0.4
Eligible: True

Error
Input: income=0, debt=500, score=700
Salida:
Error: invalid input


"""

# (CODE HERE)

print("welcome to the debt elegibility system")
while True:
    monthly_income=input("set your income\n")
    monthly_debt = input("set your monthly debt studio\n")
    credit_score = input("set your creditscore")

    try:
        income=float(monthly_income)
        debt=float(monthly_debt)
        score=int(credit_score)
        if income>0 and debt>=0 and score>=0:
            break
        else:
            print("Error: invalid input.") 
    except ValueError:
        print("please insert a valid input")
debt_ratio=debt/income
if income >=8000.0 and debt_ratio<=.4 and score>=650:
    elegible=True
else:
    elegible= False
#salidas    
print(f"Debt ratio: {round(debt_ratio,2)}")
print(f"Eligible: {elegible}")

"""
PROBLEM 6: Body Mass Index (BMI) and category flag
Description:
Calculates BMI and evaluates whether a person is underweight, normal, or
overweight using boolean flags.
Inputs:
weight_kg (float)
height_m (float)
Outputs:
"BMI:" <bmi_rounded>
"Underweight:" true|false
"Normal:" true|false
"Overweight:" true|false
Validations:
weight_kg > 0.0
height_m > 0.0
Otherwise print "Error: invalid input".

test cases

Normal
Input: weight=70, height=1.75
Salida:
BMI: 22.86
Underweight: False
Normal: True
Overweight: False

Border
Input: weight=50, height=1.70
Salida:
BMI: 17.30
Underweight: True
Normal: False
Overweight: False

Error
Input: weight=-60, height=1.70
Salida:
Error: invalid input

 """

#(CODE HERE)

print("welcome to the BMI index calculator")
is_underweight=False
is_normal=False
is_overweight = False
while True:
    weight_kg = input("set your weight in kilograms\n ")
    height= input("set your heigh in meters")
    valid=False
    try:
        Weight = float( weight_kg)
        h =float( height)
        valid=True
    except ValueError:
        print("error : invalid input")
    if not valid or Weight<=0.0 or h<=0.0: 
        print("Error:invalid input")
    else:
        break

bmi=Weight/(h*h)
if bmi< 18.5:
    is_underweight=True
elif bmi>=18.5 and bmi<25:
    is_normal=True
else:
    is_overweight=True

print(f"BMI:{round(bmi,2)}")
print(f"Underweight: {is_underweight}")
print(f"Normal: {is_normal}")
print(f"Overweight: {is_overweight}")

# CONCLUSIONS
"""
Integers and floats work together in many real-life calculations, allowing
programs to model quantities, rates, and ratios. Boolean values arise from
comparisons and form the basis of decisions through if-statements. Proper
validation prevents incorrect results and runtime errors such as division by
zero or negative values where they are not allowed. Logical operators like
and, or, and not enable complex conditions such as discount eligibility,
loan approval, and category classification. These patterns are present in
payroll systems, financial evaluations, and measurement tools.
"""

# REFERENCES
"""
Python Software Foundation.
Python Documentation – Built-in Types: Numeric Types (int, float, complex).
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Python Software Foundation.
Boolean Type — bool.
https://docs.python.org/3/library/stdtypes.html#truth-value-testing

Python Software Foundation.
Input and Output — The input() function.
https://docs.python.org/3/library/functions.html#input

*Python Documentation – Expressions and Operators.
(Arithmetic, comparison, logical operators)
https://docs.python.org/3/reference/expressions.html

Real Python.
Understanding Data Types in Python (Numbers, Booleans, Type Casting).
https://realpython.com/python-data-types/

W3Schools Python Tutorial.
Python If…Else, Logical Operators, and Conditions.
https://www.w3schools.com/python/python_conditions.asp

Automate the Boring Stuff with Python – Chapter 2.
Flow Control, Boolean Logic, Input Validation.
https://automatetheboringstuff.com/

Think Python (Allen B. Downey).
Chapter 7–8: Loops, Conditionals, boolean expressions.
http://greenteapress.com/thinkpython2/thinkpython2.pdf
"""

# URL repository:
# https://github.com/Angel-Yahir-Hernandez-Arredondo/Tareas_metodologia.git