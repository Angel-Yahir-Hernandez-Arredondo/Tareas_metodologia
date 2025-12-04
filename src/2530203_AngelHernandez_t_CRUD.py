"""
Student Name: Angel Yahir Hernandez Arredondo
Student ID:2530203
Group: 1-3
Assignment: CRUD Project Bakery Inventory CRUD

EXECUTIVE SUMMARY
This program implements a CRUD (Create, Read, Update, Delete) system for a 
bakery inventory using Python functions. A nested dictionary structure is used 
to store each type of bread. Every key in the main dictionary represents a 
product identifier, and its value is another dictionary containing fields such 
as name, price, and remaining quantity.
The program includes:
- Creating new bread types
- Deleting existing bread types
- Updating price or quantity
- Listing all products
- Processing orders, reducing quantities, and calculating totals
The menu-driven interface allows users to interact dynamically with the 
inventory. Input validation functions prevent invalid numbers or empty fields 
from crashing the program. This CRUD demonstrates how in-memory data 
structures can be manipulated through well-defined functions.

PROBLEM DESCRIPTION
This program manages a bakery inventory containing various bread types. 
A nested dictionary (Option A) was chosen as the main structure:
products = {
    "mexican sweet bread": {
        "name": "mexican sweet bread",
        "price": 10.5,
        "quantity remaining": 20
    },
    ...
}
Reason for choosing nested dictionaries:
1) Fast lookup using product identifiers.
2) Allows grouping of product attributes in a readable way.
3) Easy to update individual fields inside each product.
4) Direct access without searching through lists.
INPUTS (AS USED IN YOUR CODE)
1. Menu option:
   - User enters by number or name: 
     "1", "new type of bread", "2", "delete type of bread", "3", etc.
2. For creating a bread type:
   - key (product identifier)
   - name (product name)
   - quantity (as string, later validated and converted to int)
   - price (as string, later validated and converted to float)
3. For deleting a bread type:
   - key (must match existing key exactly)
4. For updating:
   - key
   - price (can be empty → None)
   - quantity (can be empty → None)
5. For orders:
   - key (bread type)
   - quantity (int)
   - YES/NO confirmation-
OUTPUTS (AS PRODUCED BY YOUR CODE)-
- "your product X has been added under the key Y"
- "error: invalid input"
- "error:the key is not in the dictionary"
- "X deleted succesfully"
- "please set a valid price"
- "please set a valid quantity"
- "you cant have a negative value"
- "your quantity must not be less than 0"
- "currently we don't have X"
- "sorry we don't have enough X in inventory"
- Listing of all products with all fields printed
- Total cost after placing an order

REALISTIC TEST CASES (BASED ON YOUR PROGRAM BEHAVIOR)

TEST CASE 1 — NORMAL 
User selects: 1 (new type of bread)
Inputs:
  key = "banana bread"
  name = "banana bread"
  quantity = "15"
  price = "22"
Expected program behavior:
  - input_validation() converts price→22.0, quantity→15
  - adding_bread_type() adds the new dictionary entry
Program Output:
  "your product banana bread has been added under the key banana bread"
  Then listing() prints all products including the new one:
      product: banana bread
       name: banana bread
       price: 22.0
       quantity remaining: 15

TEST CASE 2 — BORDER CASE 
User selects: 3 
Inputs:
  key = "donut"
  price = ""     (empty → means do not update)
  quantity = "100"
Expected program behavior:
  - input_validation() returns price=None, quantity=100
  - updating_quantity_or_price() updates only "quantity remaining"
Program Output:
  (prints donut's updated fields)
   name donut
   price 8.5
   quantity remaining 100

TEST CASE 3 — ERROR CASE 
User selects: 1 (new type of bread)
Inputs:
  key = "badbread"
  name = "bad bread"
  quantity = "5"
  price = "abc"
Expected program behavior:
  - input_validation() detects price cannot convert to float
Program Output:
  "please set a valid price"
  Item is NOT added
"""
#CRUD  ventas de pan(inventario):

def adding_bread_type(key:str,name:str,price:float,quantity:int):
    """
    Docstring for adding_bread_type:
    this function adds a new index to the main dictionary
    :param key: main index's main identifier
    :type key: str
    :param name: name of the type of product(bread) this index contains
    :type name: str
    :param price: cost per piece
    :type price: float
    :param quantity: units in existence
    :type quantity: int
    """
    if key in products or name.strip()=="" or price<0 or quantity<0:
        print("error: invalid input")
        return
    products[key]={
          "name":name,
         "price":price,
         "quantity remaining":quantity,
         }
    print(f"your product {name} has been added under the key {key}")

def deleting_obsolete(key:str,):
        """
        Docstring for deleting_obsolete
        :this function is used to delete an index from our main dictionary
        :param key: Description
        :type key: str
        """
        if key not in products:
             print("error:the key is not in the dictionary")
             return(False)
        else:
            products.pop(key)
            print(f"{key} deleted succesfully")
            return(True)
        
def updating_quantity_or_price(key:str,price:float=None,quantity:int=None):
     """
     Docstring for updating_quantity_or_price:
     this function updates the price or quantity of a product in the dictionary
     
     :param key: product which we want to actualize
     :type key: str
     :param price: price to which we want to adjust our price
     :type price: float
     :param quantity: quantity in existance
     :type quantity: int
     """
     
     if key not in products:
            print("please set a valid input")
            return(False)
     if key in products and price is not None:
        if price>=0:
            products[key]["price"]=price
        else:
          print("you cant have a negative value")
          return(False)
     if key in products and quantity is not None:
        if quantity>=0:
            products[key]["quantity remaining"]=quantity
        else:    
            print("your quantity must not be less than 0")
            return(False)
     return(True)

def finalization(ans:str,):
    """
    Docstring for listing:
    this function allows us to exit a loop and finish the program:
    :param ans: a simple YES or NO
    :type ans: str
    """
    ans=ans.strip().upper()
    if ans=="YES":
        return False
    elif ans=="NO":
        return True
    else:
        print("please set a valid input")

def listing():
     """
     Docstring for listing
     this function allows us to view the description of every product:
     """
     for key, data in products.items():
          print(f"product: {key}")
          for attr, value in data.items():
               print(f" {attr}: {value}")

def order(bread:dict,):
     """
     Docstring for order
     this function receives a dictionary containing
     types of bread we want to buy and the quantity
     of bread we need and calculates the price we'd
     need to pay to get that order.
     :param bread: dictionary containing our information.
     :type bread: dict
     """
     total=0
     for key, quantity in bread.items():
        if key in products:
            existence=products[key]["quantity remaining"]
            if quantity <= existence:
                total=total+quantity*products[key]["price"]
                products[key]["quantity remaining"]-= quantity
                    
            else:
                print(f"sorry we don't have enough {key} in inventory")
                print(f"currently we only have {existence} pieces of {key}")
        else:
            print(f"currently we don't have {key}")                         
     return(total)

def menu (option:str):
     """
     Docstring for menu:
     this function help us to select an option
     from the menu and discard invalid inputs
     :param option: Description
     :type option: str
     """
     if option not in options and option not in options.values():
          print("please set a valid input")
          return None
     for key,data in options.items():
        if key == option or data == option :
            function=data
            return(function)

def input_validation(price, quantity):
        """
        Docstring for input_validation
        this function is used to verify that our inputs are
        valid to process in the rest of our problem
        :param price: Description
        :param quantity: Description
        """
        if not price.strip()=="":
            try:
                price=float(price)   
            except:
                print("please set a valid price")
                return False , None, None
        else:
            price=None
        if not quantity.strip()=="":
                 try:
                     quantity=int(quantity)
                 except ValueError:
                     print("please set a valid quantity")
                     return False, None, None
        
        return True, price, quantity
                
products={
    "mexican sweet bread":{"name":"mexican sweet bread",
                            "price":10.5,
                            "quantity remaining": 20},
    "donut":{"name":"donut",
            "price":8.50,
            "quantity remaining": 30,},
    "biscuit":{"name":"biscuits",
            "price":7.50,
            "quantity remaining": 10,},
    "mexican bread roll":{"name":"mexican bread roll",
            "price":3.50,
            "quantity remaining": 98,},
    "croissant":{"name":"croissant",
            "price":12.00,
            "quantity remaining": 98,},
    "lovers bread":{"name":"lovers bread",
            "price":20.00,
            "quantity remaining": 50,},
    "piggy cookies":{"name":"piggy cookies",
            "price":15.00,
            "quantity remaining": 54,},
    "cup cakes":{"name":"cupcake",
            "price":20.00,
            "quantity remaining": 28,},
    "palmiers":{"name":"palmiers",
            "price":17.50,
            "quantity remaining": 94,},
    "brioche bread":{"name":"brioche bread",
            "price":25.00,
            "quantity remaining": 67,},
}

options={
    "1": "new type of bread",
    "2": "delete type of bread",
    "3":"update inventory",
    "4":"calculate order",
    "5":"itiems",
    "6": "exit",
}


print("welcome to the inventory interface")
keep_going=True
while keep_going:
    print("main menu\n")
    for key, data in options.items():
        print(f"{key}- {data}\n")
    print("indicate by their name or number")
    option=input("which action would you like to do?\n").strip().lower()
    operation=menu(option)
    if operation == None:
        ans=input("do you wish to try again?")
        keep_going=finalization(ans)
    elif operation == "new type of bread":
         print("welcome to the addition menu")
         key=input("please set your new product's identifier\n")
         name=input("please now set your products name \n")
         valid=False
         while not valid:
            quantity=input("please set your product's inventory\n")
            price=input("please now set your products price\n")
            touple=input_validation(price, quantity)
            if touple [0] != False:
                 valid=touple[0]
                 price=touple[1]
                 quantity=touple[2]
                 adding_bread_type(key, name, price, quantity)
                 listing()
         
    elif operation == "delete type of bread":
         print("welcome to the deleting menu.\n here you can delete a product of your choice")
         print(f"we currently have \n")
         listing()
         valid=False
         while not valid:
            key = input("please set the type of bread you need to delete:\n")
            valid=deleting_obsolete(key)
         listing()

    elif operation == "update inventory":
         print("welcome to the updating menu.\n here you can update the price and quantity of our products")
         print(f"we currently have \n")
         listing()
         print("if you  only wish to update one aspect just leave the other blank")
         valid=False
         while valid==False:
            key= input("write the name of the product you'd like to update\n")
            price=input("set the new price\n")
            quantity= input("set the current existence of the product\n")
            touple=input_validation(price, quantity)
            if touple[0] != False:
                price=touple[1]
                quantity=touple[2]
                valid=updating_quantity_or_price(key, price, quantity)
                for index, datum  in products[key].items():
                     print(index,datum)
    elif operation == "calculate order":
         print ("welcome to the order menu")
         print("our current products are")
         listing()
         print("set your products specifying type and quantity\n IMPORTANT:set values one by one")
         ans=True
         bread ={}
         total_order={}
         total=0
         while ans:
            key=input("please set your type of bread\n")
            quantity=input("set how many pieces do you need?")
            try:
                quantity=int(quantity)
            except ValueError:
                 print("error invalid quantity")
                 continue
            if quantity>=0:
                bread={key:quantity}
                total_order.update(bread)
                price=order(bread)
                total=total+price
                ans2=None
                while ans2==None:
                    decision= input("is that your total order?\n YES or NO")
                    ans=finalization(decision)
                    ans2=ans
         for key,data in total_order.items():
              print(key,data)
         print(total)


    elif operation == "itiems":
         listing()
    elif operation == "exit":
         ans=input("are you sure you want to exit the program?\n" \
         "YES OR NO\n")
         keep_going=finalization(ans)
         print("have a nice day")
"""
CONCLUSIONS
The CRUD structure made the inventory system organized, separating creation, 
deletion, updating, and ordering into their own functions. This modularity 
improves clarity and reduces errors. Nested dictionaries worked efficiently 
because each bread type could be accessed instantly by its identifier and 
updated easily.
A significant challenge was input validation, especially when converting 
price and quantity from raw user input. The validation function helped 
prevent invalid conversions and improved program safety.
This CRUD can be extended to persistent storage by saving the dictionary 
into a JSON file or interacting with a database for long-term inventory 
management.

REFERENCES
1) Python Documentation – Data Structures (dict, list)
   https://docs.python.org/3/tutorial/datastructures.html
2) Python Documentation – Functions
   https://docs.python.org/3/tutorial/controlflow.htmlefining-functions
3) CRUD in Python (RealPython)
   https://realpython.com/python-dicts/

4) Handling User Input in Python
   https://realpython.com/python-input-output/

5) Exception Handling in Python
   https://docs.python.org/3/tutorial/errors.html
"""

# URL repository:
# https://github.com/Angel-Yahir-Hernandez-Arredondo/Tareas_metodologia.git