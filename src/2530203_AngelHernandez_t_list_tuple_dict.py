"""
Management of Lists, Tuples, and Dictionaries in Python
Angel Yahir Hernandez Arredondo
2530203
IM 1-3
------------------------------------------------------------
EXECUTIVE SUMMARY
------------------------------------------------------------
This document presents six problems designed to practice Python 
collections: lists, tuples, and dictionaries. A list is an ordered 
and mutable collection, useful when it is necessary to add, remove, 
or modify elements. A tuple is ordered but immutable, which makes it 
ideal for fixed records such as coordinates or constant data sets. 
A dictionary stores key-value pairs, enabling fast lookups through 
a descriptive key.

Each problem includes input and output design, validation rules, and 
test cases that demonstrate practical applications such as shopping 
lists, product catalogs, grade management, word frequency counting, 
and a simple contact directory. The document highlights how collections 
help organize, process, and retrieve data efficiently in real-world 
programs.

------------------------------------------------------------
------------------------------------------------------------
GOOD PRACTICES AND PRINCIPLES (STRINGS)
------------------------------------------------------------
- Strings are immutable: any modification creates a new string.
- Always normalize input with strip() and lower() before comparing it.
- Avoid magic numbers when slicing; document each slice clearly.
- Prefer built-in string methods instead of rewriting basic logic.
- Validation order matters: first check empty input, then structure.
- Write clean code with descriptive variable names and clear messages.

"""
"""
Problem 1:
------------------------------------------------------------
Description:
This program works with a shopping list created from an input string.
It creates an initial list, adds a new item, counts the total items,
and checks if a specific product is in the list.

Inputs:
- initial_items_text: string with items separated by commas
- new_item: string of the new product to add
- search_item: product name to search in the list

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- initial_items_text must not be empty after strip()
- split items and clean spaces using strip()
- new_item and search_item must not be empty

Test cases:
1) Normal:
    Input: "apple, banana, orange", "grape", "banana"
    Output: Items list: ['apple', 'banana', 'orange', 'grape']
            Total items: 4
            Found item: true

2) Border:
    Input: "apple", "pear", "watermelon"
    Output: Items list: ['apple', 'pear']
            Total items: 2
            Found item: false

3) Error:
    Input: "   ", "pear", "apple"
    Output: Error: invalid input
"""
initial_items_text = input("Enter initial items separated by commas: ")
new_item = input("Enter new item to add: ")
search_item = input("Enter item to search: ")

initial_items_text = initial_items_text.strip()
new_item = new_item.strip()
search_item = search_item.strip()

if initial_items_text == "" or new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    
    items_list = [item.strip() for item in initial_items_text.split(",")]

    items_list.append(new_item)

    total_items = len(items_list)

    is_in_list = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", total_items)
    print("Found item:", str(is_in_list).lower())

"""
Problem 2:
------------------------------------------------------------
Description:
This program reads the coordinates of two points in 2D space,
creates two tuples, calculates the distance between them,
and computes the midpoint tuple.

Inputs:
- x1, y1: float coordinates of point A
- x2, y2: float coordinates of point B

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validations:
- All four inputs must be valid float numbers

Test cases:
1) Normal:
    Input: 0, 0, 4, 3
    Output: Point A: (0.0, 0.0)
            Point B: (4.0, 3.0)
            Distance: 5.0
            Midpoint: (2.0, 1.5)

2) Border:
    Input: 1.5, 1.5, 1.5, 1.5
    Output: Point A: (1.5, 1.5)
            Point B: (1.5, 1.5)
            Distance: 0.0
            Midpoint: (1.5, 1.5)

3) Error:
    Input: "abc", 2, 3, 4
    Output: Error: invalid input
"""

x1_text = input("Enter x1: ")
y1_text = input("Enter y1: ")
x2_text = input("Enter x2: ")
y2_text = input("Enter y2: ")

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)
except:
    print("Error: invalid input")
else:
    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = (((x2 - x1)*2 + (y2 - y1)*2)*0.5)
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

"""
Problem 3:
------------------------------------------------------------
Description:
This program manages a small product catalog using a dictionary.
It reads a product name and a quantity, checks if the product exists,
and calculates the total price. If the product is not found,
it displays an error message.

Inputs:
- product_name: string
- quantity: int

Outputs:
- If product exists:
    "Unit price:" <unit_price>
    "Quantity:" <quantity>
    "Total:" <total_price>
- If product does not exist:
    "Error: product not found"

Validations:
- product_name must not be empty after strip()
- quantity must be a valid integer > 0
- product_name must be a key in the dictionary

Test cases:
1) Normal:
    product_name = "apple", quantity = 3
    Output: Unit price: 10.0
            Quantity: 3
            Total: 30.0

2) Border:
    product_name = "milk", quantity = 1
    Output: Unit price: 15.5
            Quantity: 1
            Total: 15.5

3) Error:
    product_name = "unknown", quantity = 2
    Output: Error: product not found
"""

product_prices = {
    "apple": 10.0,
    "milk": 15.5,
    "bread": 12.0
}

product_name = input("Enter product name: ").strip()
quantity_text = input("Enter quantity: ")

if product_name == "":
    print("Error: invalid input")
else:
    try:
        quantity = int(quantity_text)
        if quantity <= 0:
            print("Error: invalid input")
        else:
            if product_name in product_prices:
                unit_price = product_prices[product_name]
                total_price = unit_price * quantity

                print("Unit price:", unit_price)
                print("Quantity:", quantity)
                print("Total:", total_price)
            else:
                print("Error: product not found")
    except:
        print("Error: invalid input")

"""
Problem 4:
------------------------------------------------------------
Description:
This program manages student grades using a dictionary where each
key is a student's name and each value is a list of float grades.
It reads a student's name, calculates their average, and determines
if they passed with a boolean (average >= 70.0).

Inputs:
- student_name: string

Outputs:
- If student exists:
    "Grades:" <grades_list>
    "Average:" <average>
    "Passed:" true|false
- If student does not exist:
    "Error: student not found"

Validations:
- student_name must not be empty after strip()
- student_name must exist in the dictionary
- the grade list must not be empty

Test cases:
1) Normal:
   Input: student_name = "Alice"
   Output: Grades: [90, 85, 88]
           Average: 87.67
           Passed: true

2) Border:
   Input: student_name = "Mark" (grades: [70])
   Output: Grades: [70]
           Average: 70.0
           Passed: true

3) Error:
   Input: student_name = "Unknown"
   Output: Error: student not found
"""

students_grades = {
    "Alice": [90, 85, 88],
    "Bob": [60, 72, 68],
    "Mark": [70]
}

student_name = input("Enter student name: ").strip()

if student_name == "":
    print("Error: invalid input")
else:
    if student_name in students_grades:
        grades_list = students_grades[student_name]

        if len(grades_list) == 0:
            print("Error: student not found")  # No grades to calculate
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = (average >= 70.0)

            print("Grades:", grades_list)
            print("Average:", round(average, 2))
            print("Passed:", str(is_passed).lower())
    else:
        print("Error: student not found")

"""
Problem 5:
------------------------------------------------------------
Description:
This program reads a sentence, converts it to lowercase, splits it
into a list of words, and counts the frequency of each word using
a dictionary. It also finds the most common word in the sentence.

Inputs:
- sentence: string

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word>

Validations:
- sentence must not be empty after strip()
- words list must not be empty after splitting
- punctuation is removed using replace() as a simple decision

Test cases:
1) Normal:
   Input: "Apple banana apple orange"
   Output: Words list: ['apple', 'banana', 'apple', 'orange']
           Frequencies: {'apple': 2, 'banana': 1, 'orange': 1}
           Most common word: apple

2) Border:
   Input: "Hello"
   Output: Words list: ['hello']
           Frequencies: {'hello': 1}
           Most common word: hello

3) Error:
   Input: "" (empty sentence)
   Output: Error: invalid input
"""

sentence = input("Enter a sentence: ").strip()


if sentence == "":
    print("Error: invalid input")
else:
    
    sentence = sentence.lower()
    sentence = sentence.replace(",", "").replace(".", "").replace("!", "").replace("?", "")

    words_list = sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common = None
        highest_count = 0

        for w in freq_dict:
            if freq_dict[w] > highest_count:
                highest_count = freq_dict[w]
                most_common = w

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common)

"""
Problem 6
------------------------------------------------------------
Description:
Implement a simple contact book using a dictionary where:
- key: contact name (string)
- value: phone number (string)
The program must:
  1) Read an action ("ADD", "SEARCH", "DELETE")
  2) For ADD → read name and phone, save or update
  3) For SEARCH → read name and show phone if exists
  4) For DELETE → read name and delete if exists

Inputs:
- action_text (string)
- name (string, depends on action)
- phone (string, only for ADD)

Outputs:
- ADD:
      "Contact saved:" name, phone
- SEARCH:
      if exists: "Phone:" <phone>
      else: "Error: contact not found"
- DELETE:
      if exists: "Contact deleted:" name
      else: "Error: contact not found"

Validations:
- action_text must be ADD, SEARCH, or DELETE (uppercase)
- name must not be empty
- phone must not be empty if action is ADD

Test cases:
1) Normal:
   Input:
      ADD
      Pedro
      12345
   Output:
      Contact saved: Pedro, 12345

2) Border:
   Input:
      SEARCH
      Alice
   Output:
      Phone: <phone>

3) Error:
   Input:
      SEARCH
      Jose
   Output:
      Error: contact not found
"""

contacts = {
    "Alice": "1234567890",
    "Bob": "5551112222",
    "Carlos": "9876543210"
}

action_text = input("Action (ADD / SEARCH / DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    name = input("Name: ").strip()

    if not name:
        print("Error: name cannot be empty")
    else:

        if action_text == "ADD":
            phone = input("Phone: ").strip()

            if not phone:
                print("Error: phone cannot be empty")
            else:
                contacts[name] = phone
                print("Contact saved:", name + ",", phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")

"""
------------------------------------------------------------
CONCLUSION
------------------------------------------------------------
Lists, tuples, and dictionaries serve different purposes in Python. 
Lists are ideal when data needs to be modified frequently, as they allow 
adding, removing, and updating elements with great flexibility. Tuples are 
useful for storing fixed data that should not change, such as coordinates 
or configuration values. Dictionaries make lookups efficient because each 
value is accessed through a specific key, avoiding the need to search 
through the entire structure.

When these collections are combined, common patterns emerge—such as 
dictionaries that store lists—which make it possible to group information 
while still accessing it quickly through keys.

------------------------------------------------------------
REFERENCES
------------------------------------------------------------
https://ellibrodepython.com/tuplas-python

https://elpythonista.com/tuplas-en-python-tuple

https://ellibrodepython.com/listas-en-python

https://ebac.mx/blog/listas-en-python

https://ellibrodepython.com/diccionarios-en-python
"""

# URL repository:
# https://github.com/Angel-Yahir-Hernandez-Arredondo/Tareas_metodologia.git