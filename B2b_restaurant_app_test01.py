# -*- coding: utf-8 -*-
"""
# ------------------------------- Imports -------------------------------

here we place the libraries we are importing
"""

import datetime
import re


# ----- Global variables area --------------------------------------------------------
# here we place variables that are visible throughout the whole program
# Var to store all the customer selection
items_selection = []

user_login = [] # list that will store all the customer data
## William Update - store order objects
orders = []

# var to store all the total amount
amtTotal = 0

SIGN_UP = 200
SIGN_IN = 201
ORDER_TYPE_SELECTION = 202
# -----------------------------------------------------------------------------------

"""# ------------------------------- Area for Class Definition -------------------------------

Here we place different class definitions we may be using
"""

# PRODUCT ----------------------------------------------------------------------
class Product:

  # Creating the menu list for Food and Drink to reduce the amount of code.
    # The products will be already loaded on the system.

    # drinkD = ['Coffee', 'Colddrink', 'Shake ', 'for Checkout']
    # drinkP = [2, 4, 6]

    # foodD = ['Noodles', 'Sandwich', 'Dumpling', 'Muffins', 'Pasta   ', 'Pizza    ', 'for Drinks Menu:']
    # foodP = [2, 4, 6, 8, 10, 20]
    # count = 1

    # ----------------- Initialser/constructor area
    # def __init__(self):
    #     pass

    # ----------------- method area

    # def display_food_menu(self):
        #i = 0
    #    print("--------- Food Menu Choices --------\n")

    #    for i in range(len(Product.foodD)):
    #        if i < 6:
    #            print("Enter ", Product.count, Product.foodD[i], "\t \t Price AUD ", Product.foodP[i])
    #            Product.count += 1
    #        else:
    #            print("Enter ", Product.count, Product.foodD[i])
    # def select_food_menu(self, select_items):


    #    if 1 <= select_items <= len(self.foodD):
    #        order = [Product.foodD[select_items -1], Product.foodP[select_items -1]]
    #        items_selection.append(order)
    #    else:
    #        print("Invalid Food item")
    # def display_drink_menu(self):
    #    Product.count = 1
    #    print("--------- Drink Menu Choices --------\n")
    #    for i in range(len(Product.drinkD)):
    #        if i < 3:
    #            print("Enter ", Product.count, self.drinkD[i], "\t \t Price AUD ", self.drinkP[i])
    #            Product.count += 1
    #        else:
    #            print("Enter ", Product.count, Product.drinkD[i])
    # def select_drink_menu(self, select_items):

    #    if 1 <= select_items <= len(self.drinkD):
    #        order = [Product.drinkD[select_items -1], Product.drinkP[select_items - 1]]
    #        items_selection.append(order)
    #    else:
    #        print("Invalid Drink item")
    # def display_items_selection(self):
        # for i in items_selection:
        #     print(i)
    #    print(items_selection)

  def __init__(self, name, price, prod_type):
    self.__name = name
    self.__price = price
    self.__prod_type = prod_type

  def get_product_details(self):
    return self.__name.ljust(10, " ") + (str(self.__price) + " AUD").rjust(5, " ")

  def get_price(self):
    return self.__price

# CUSTOMER ---------------------------------------------------------------------
class Customer:
  def __init__(self, name, mobile, address, date_of_birth, password):
    self.__name = name
    self.__mobile = mobile
    self.__address = address
    self.__date_of_birth = date_of_birth
    self.__password = password

  def show_customer_details(self):
    return f"Thank you, {self.__name} your id , {self.__mobile}"

  def validate_sign_in(self, mobile, password):
    return self.__mobile == mobile and self.__password == password

  def get_mobile(self):
    return self.__mobile

  def get_address(self):
    return self.__address

  def validate_name(customer_name):
    nameRegexPattern = "^[A-Za-z\-\_]{1,35}(\s[A-Za-z]{0,35})?$"
    ret_string = True
    match = re.search(nameRegexPattern, customer_name)
    if not match:
      ret_string = "\nIncorrect name pattern. Names should only be alphabets, - or _."

    return ret_string

  def validate_mobile(mobile, customer_list):
    mobileRegexPattern = "^[0-9]{10}$"
    ret_string = True
    match = re.search(mobileRegexPattern, mobile)
    if match:
      for customer in customer_list:
        if(customer.get_mobile() == mobile):
          ret_string = "\nMobile Number already exists!. Please try again."
          break
    else:
      ret_string = "\nPlease enter 10 digit mobile number starting with 0."

    return ret_string

  def validate_date_of_birth(date_of_birth):
    dobRegexPattern = "^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[1,2])/(19|20)[0-9]{2}$"
    match = re.search(dobRegexPattern, date_of_birth)
    ret_string = True
    if match:
      if ((int(date_of_birth[6:]) % 4 == 0 and int(date_of_birth[6:]) % 100 != 0)
        or int(date_of_birth[6:]) % 400 == 0):
        dobLeapRegexPattern = "^(0[1-9]|[12][0-9])/(0[1-9]|1[1,2])/(19|20)[0-9]{2}$"
        match = re.search(dobLeapRegexPattern, date_of_birth)
        if not match:
          ret_string = "\nPlease enter date in format dd/mm/yyyy."
    else:
      ret_string = "\nPlease enter date in format dd/mm/yyyy."

    return ret_string

  def validate_password(password, confirm_password):
    ret_string = True
    if password == confirm_password:
      passwordRegexPattern = "^[a-zA-Z]*[@|&|#][0-9]*$"
      match = re.search(passwordRegexPattern, password)
      if not match:
        ret_string = "\nIncorrect password pattern. Password should"\
        " start with alphabet followed by @, & or # and ends with numbers."
    else:
      ret_string = "\nYour passwords are not matching.\n"\
                "Please try again.\n"

    return ret_string

class Order:

  def __init__(self, customer, current_order_id):
    self.__order_id = current_order_id + 1
    self.__customer = customer
    self.__date_transaction = datetime.datetime.today().strftime("%d/%m/%Y")
    self.__product_list = []
    self.__total_amount = 0
    self.order_type = "Order"

  # This method will create a customer history
  def create_order_data(self):

      user_login.append(self.order_id_generate())
      # user_login.append(self.customerMobile)
      # user_login.append(items_selection)
      user_login.append(self.date)


      for i in items_selection:
            self.totalOrder_amount += i[1]

      amount = self.totalOrder_amount
      user_login.append(amount)
      user_login.append(self.orderType)

  def add_food(self, product: Product):
    self.__product_list.append(product)

  def get_order_id(self):
    return self.__order_id

  def get_products(self):
    return self.__product_list

  def get_date(self):
    return datetime.datetime.strptime(self.__date_transaction,"%d/%m/%Y")

  def get_total_amount(self):
    return self.__total_amount

  def get_order_summary(self, report_type):
    report = ""

    report = "\nOrder ID\tDate\t     Total Amount Paid\tType of Order"
    if(report_type == "DineIn"):
        for order in orders:
            if order.__customer.get_mobile() == customer.get_mobile() and order.order_type == "DineIn":
                report += "\n"+str(order.get_order_id()).ljust(12," ")+order.get_date().strftime("%d/%m/%Y").ljust(13," ")+str(order.get_total_amount()).ljust(19," ")+order.order_type

    elif(report_type == "PickUp"):
        for order in orders:
            if order.__customer.get_mobile() == customer.get_mobile() and order.order_type == "PickUp":
                report += "\n"+str(order.get_order_id()).ljust(12," ")+order.get_date().strftime("%d/%m/%Y").ljust(13," ")+str(order.get_total_amount()).ljust(19," ")+order.order_type

    elif(report_type == "Delivery"):
        for order in orders:
            if order.__customer.get_mobile() == customer.get_mobile() and order.order_type == "Delivery":
                report += "\n"+str(order.get_order_id()).ljust(12," ")+order.get_date().strftime("%d/%m/%Y").ljust(13," ")+str(order.get_total_amount()).ljust(19," ")+order.order_type

    elif(report_type == "All"):
        report_list = []
        for order in orders:
            if order.__customer.get_mobile() == customer.get_mobile() and order.order_type in ("DineIn","PickUp","Delivery"):
                temp_list = []
                temp_list.append(order.get_order_id())
                temp_list.append(order.get_date())
                temp_list.append(order.get_total_amount())
                temp_list.append(order.order_type)
                report_list.append(temp_list)

        report_list.sort(key = lambda x:x[1], reverse = False)

        for i in report_list:
            report += "\n"+str(i[0]).ljust(12," ")+i[1].strftime("%d/%m/%Y").ljust(13," ")+str(i[2]).ljust(19," ")+i[3]

    elif(report_type == "Total"):
        total_amount = 0
        for order in orders:
            if (order.__customer.get_mobile() == customer.get_mobile() and order.order_type in ("DineIn","PickUp","Delivery")):
                total_amount = total_amount + order.get_total_amount()

            report = "\nTotal Amount spend on all orders AUD: "+str(total_amount)

    return report

class DineIn(Order):

  def __init__(self, customer, current_order_id):
    super().__init__(customer, current_order_id)
    self.__drinks = []
    self.order_type = "DineIn"

  def display_dine_in_customer(self):
      print("Customer ID", self.id)

  def dineIn_futher_detials(self):
      print("-------- Dine-In details ---------")
      Dine_In.numberCustomer = int(input("Enter number of customer: "))
      Dine_In.dateVisit = input("Enter date of visit: ")
      Dine_In.timeVisit = input("Enter time of visit: ")


      print("Thank You for entering the details, Your Booking is confirmed.")

  def add_drink(self, product: Product):
    self.__drinks.append(product)

  def get_drinks(self):
    return self.__drinks

  def get_dinein_charge(self):
    total_amount = 0.0
    for product in self.get_products():
      total_amount = total_amount + product.get_price()

    for drink in self.__drinks:
      total_amount = total_amount + drink.get_price()

    return total_amount * 0.15

  def calculate_total_amount(self):
    total_amount = 0.0
    for product in self.get_products():
      total_amount = total_amount + product.get_price()

    for drink in self.__drinks:
      total_amount = total_amount + drink.get_price()

    self.__total_amount = total_amount * 0.15 + total_amount

    return self.__total_amount

class PickUp(Order):

  def __init__(self, customer, current_order_id):
    super().__init__(customer, current_order_id)
    self.order_type = "PickUp"

  def pickUp_unique_code(self):

      unique_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

      self.unique_code_order = "B" + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers))
      return self.unique_code_order


  def pickUp_futher_detials(self):
      print("-------- Pick-Up detials ---------")
      Pick_Up.nameCustomer = input("Enter name of customer: ")
      Pick_Up.datePickup = input("Enter date of pick up: ")
      Pick_Up.timePickup = input("Enter time of pick up: ")

      # Printing message
      print("Thank You for entering the details, Your Booking is confirmed.")
      print("Order confirmation code: ", self.pickUp_unique_code())

  def calculate_total_amount(self):
    total_amount = 0.0
    for product in self.get_products():
      total_amount = total_amount + product.get_price()

    self.__total_amount = total_amount

    return self.__total_amount

class Delivery(Order):

  def __init__(self, customer, current_order_id):
    super().__init__(customer, current_order_id)
    self.__distance = 0
    self.order_type = "Delivery"

  def delivery_distance_calculation(self):

      if (Delivery.distanceDely >= 0 and Delivery.distanceDely <= 4):
          print(" Delivery charge will be 3$.")
      elif (Delivery.distanceDely > 4 and Delivery.distanceDely <= 8):
          print(" Delivery charge will be 6$.")
      elif (Delivery.distanceDely > 8 and Delivery.distanceDely <= 12):
          print(" Delivery charge will be 10$.")
      elif (Delivery.distanceDely > 12):
          print(" No delivery can be done.")

# Unique code method generate
  def delivery_unique_code(self):

      unique_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

      self.unique_code_order = "B" + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers))
      return self.unique_code_order

  def delivery_further_details(self):

      print("-------- Delivery details ---------")
      Delivery.distanceDely = int(input("Enter the distance in KM: "))
      Delivery.delivery_distance_calculation(self.distanceDely)
      Delivery.dateDely = input("Enter delivery date: ")
      Delivery.timeDely = input("Enter delivery time: ")

      #Creating a validtion condition to check each input from the user

      #Printing message
      print("Thank You for entering the details, Your Booking is confirmed.")
      print("Order confirmation code: ", self.delivery_unique_code())

  def display_delivery_customer(self):
      print(self.id)
      print(self.distanceDely)
      print(self.dateDely)
      print(self.timeDely)
      print(self.delivery_unique_code())

  def set_distance(self, distance_in_km):
    self.__distance = distance_in_km

  def calculate_delivery_charge(self):
    delivery_charge = 0
    if(self.__distance > 0 and self.__distance <= 4):
      delivery_charge = 3
    elif(self.__distance > 4 and self.__distance <= 8):
      delivery_charge = 6
    elif(self.__distance > 8 and self.__distance <= 12):
      delivery_charge = 10
    elif(self.__distance > 12):
      delivery_charges = None

    return delivery_charge

  def calculate_total_amount(self):
    total_amount = 0.0
    for product in self.get_products():
      total_amount = total_amount + product.get_price()

    self.__total_amount = total_amount * 0.15 + total_amount

    return self.__total_amount

"""# ------------------------------- Function Area -------------------------------

here we place definitions for general functions
"""

def function_selector(current_menu):
  repeat_counter = 0
  running = True
  while(running):
    if current_menu == SIGN_UP:
      customer = sign_up(customers)
      if(type(customer) == tuple):
        print("\n\nSign up failed, input errors")
        repeat_counter += 1
        for item in customer:
          if(item != True):
            print(item)
      else:
        customers.append(customer)
        running = False
      if repeat_counter > 3:
        running = False

    elif current_menu == SIGN_IN:
      sel = user_menu()
      if(sel == "2.1"):
        function_selector(ORDER_TYPE_SELECTION)
        running = False
      elif(sel == "2.2"):
        ## William Update - Report
        report_choice = report_menu()
        show_report(report_choice)
        ## End update
      elif(sel == "2.3"):
        print("Logging Out...\nThank you for using our app...\n\n")
        current_customer = None
        running = False
      else:
        print("You entered an invalid selection...\nPlease enter again...\n\n")
    elif current_menu == ORDER_TYPE_SELECTION:
      start_ordering()
      running = False

def top_menu():
  print("B2B Restaurant Mobile Application")
  print("[1] Sign Up")
  print("[2] Sign In")
  print("[3] Quit Application")
  user_choice = input("Please enter your choice: ")
  return user_choice

def user_menu():
  print("\n\nPlease enter 2.1 to Start Ordering.")
  print("Please enter 2.2 to Print Statistics")
  print("Please enter 2.3 for Logout")
  user_choice = input("Please enter your choice: ")
  return user_choice

## William - Update
def report_menu():
  print("\nB2B Restaurant Mobile Application - [2.2] Statistics")
  print("[1] All Dine In Orders")
  print("[2] All Pick up Orders")
  print("[3] All Deliveries")
  print("[4] All Orders (Ascending Order)")
  print("[5] Total Amount Spent on All Orders")
  print("[6] Go to Previous Menu")
  user_choice = input("Please enter your choice: ")
  return user_choice
## End update

def sign_in(list_of_customers: list[Customer]):
  print("\n----- Customer Sign in -----\n")
  username = input("Enter Username (Mobile)".ljust(27, " ") + ": ")
  password = input("Enter Password".ljust(27, " ") + ": ")

  customer_data = None
  exists = False

  for customer in list_of_customers:
    if(customer.get_mobile() == username):
      exists = True
      if(customer.validate_sign_in(username, password)):
        customer_data = customer

  return exists, customer_data

def sign_up(list_of_customers: list[Customer]):
  print("\n----- Customer Registration -----\n")
  customer_name = input("Name".ljust(27, " ") + ": ")
  address = input("Address or blank to skip".ljust(27, " ") + ": ")
  mobile = input("Mobile Number".ljust(27, " ") + ": ")
  cust_info_is_valid = True

  name_match = Customer.validate_name(customer_name)
  mobile_match = Customer.validate_mobile(mobile, list_of_customers)

  ## Name Validation
  # nameRegexPattern = "^[A-Za-z\-\_]{1,35}(\s[A-Za-z]{0,35})?$"
  # match = re.search(nameRegexPattern, name)
  # if not match:
  #    proceed = False
  #    print("\nIncorrect name pattern. Names should only be alphabets, - or _.")

  ## Mobile Validate
  # mobileRegexPattern = "^[0-9]{10}$"
  # match = re.search(mobileRegexPattern, mobile_number)
  #if match:
  #    for customer in customer_master_list:
  #        if (customer.mobile_number == mobile_number):
  #            print("\nMobile Number already exists!. Please try again.")
  #            proceed = False
  #            break
  #else:
  #    proceed = False
  #    print("\nPlease enter 10 digit mobile number starting with 0.")

  ## DOB Validation
  # dobRegexPattern = "^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[1,2])/(19|20)[0-9]{2}$"
  # match = re.search(dobRegexPattern, date_of_birth)
  # if match:
  #    if ((int(date_of_birth[6:]) % 4 == 0 and int(date_of_birth[6:]) % 100 != 0)
  #            or int(date_of_birth[6:]) % 400 == 0):
  #        dobLeapRegexPattern = "^(0[1-9]|[12][0-9])/(0[1-9]|1[1,2])/(19|20)[0-9]{2}$"
  #        match = re.search(dobLeapRegexPattern, date_of_birth)
  #        if not match:
  #            proceed = False
  #            print("\nPlease enter date in format dd/mm/yyyy.")
  #else:
  #    proceed = False
  #    print("\nPlease enter date in format dd/mm/yyyy.")

  ## Password Validation
  # if password == confirm_password:
  #    passwordRegexPattern = "^[a-zA-Z]*[@|&|#][0-9]*$"
  #    match = re.search(passwordRegexPattern, password)
  #    if not match:
  #        proceed = False
  #        print("\nIncorrect password pattern. Password should start with alphabet followed by @, & or # and ends with numbers.")
  # else:
  #    proceed = False
  #    print("\nYour passwords are not matching.\n" \
  #          "Please try again.\n")


  password = input("Password".ljust(27, " ") + ": ")
  confirm_password = input("Confirm Password".ljust(27, " ") + ": ")

  password_match = Customer.validate_password(password, confirm_password)

  date_of_birth = input("Date of Birth (DD/MM/YYYY)".ljust(27, " ") + ": ")

  date_match = Customer.validate_date_of_birth(date_of_birth)

  if(name_match == True and mobile_match == True and password_match == True and date_match == True):
    customer = Customer(customer_name, mobile, address, date_of_birth, password)
    return customer
  else:
    return name_match, mobile_match, password_match, date_match

def start_ordering():
  running = True
  while(running):
    print("\n\nPlease Enter 1 for Dine in.")
    print("Please Enter 2 for Order Online.")
    print("Please Enter 3 to go to Login Page.")
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
      current_order_id = 0
      if len(orders) > 0:
        current_order_id = orders[len(orders) - 1].get_order_id()
      temp_order = DineIn(current_customer, current_order_id)
      order_selection(temp_order)
    elif user_choice == "2":
      order_online()
    elif user_choice == "3":
      running = False
    else:
      print("\nYour input is not in the list of choices. Please enter again\n\n")

def order_online():
  running = True
  while(running):
    print("\n\nEnter 1 for Self Pickup.")
    print("Enter 2 for Home Delivery.")
    print("Enter 3 to go to Previous Menu.")
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
      running = False
      current_order_id = 0
      if len(orders) > 0:
        current_order_id = orders[len(orders) - 1].get_order_id()
      temp_order = PickUp(current_customer, current_order_id)
      order_selection(temp_order)
    elif user_choice == "2":
      running = False
      current_order_id = 0
      if len(orders) > 0:
        current_order_id = orders[len(orders) - 1].get_order_id()
      temp_order = Delivery(current_customer, current_order_id)
      order_selection(temp_order)
    elif user_choice == "3":
      running = False
    else:
      print("\nYour input is not in the list of choices. Please enter again\n\n")

def order_selection(order: Order):
  running = True
  regex_pattern = "^[1-7]{1}$"
  while(running):
    food_count = 0
    print("\n")
    for food in foods:
      show_string = food.get_product_details()
      print("Enter " + str(food_count + 1).rjust(2, " "), show_string)
      food_count += 1
    if(order.order_type == "DineIn"):
      print("Enter " + str(food_count + 1).rjust(2, " "), "for Drinks Menu")
    else:
      print("Enter " + str(food_count + 1).rjust(2, " "), "for Checkout")
    user_choice = input("Enter your choice: ")

    if int(user_choice) == food_count + 1:
      running = False
    elif not re.search(regex_pattern, user_choice):
      print("You entered an invalid selection.\nPlease enter again.")
    else:
      order.add_food(foods[int(user_choice) - 1])

  if order.order_type != "DineIn":
    proceed_checkout(order)
    return

  running = True
  while(running):
    drink_count = 0
    print("\n")
    for drink in drinks:
      show_string = drink.get_product_details()
      print("Enter " + str(drink_count + 1).rjust(2, " "), show_string)
      drink_count += 1

    print("Enter " + str(drink_count + 1).rjust(2, " "), "for Checkout")
    user_choice = input("Enter your choice: ")

    if int(user_choice) == drink_count + 1:
      print("Goodbye")
      running = False
      proceed_checkout(order)
    elif not re.search(regex_pattern, user_choice):
      print("You entered an invalid selection.\nPlease enter again.")
    else:
      order.add_drink(drinks[int(user_choice) - 1])

def proceed_checkout(order: Order):
  running = True
  while(running):
    print("\n\nPlease Enter Y to proceed to Checkout or")
    user_choice = input("Enter N to cancel the order: ")

    if(user_choice == "Y"):
      if(order.order_type == "DineIn"):
        proceed_dinein_checkout(order)
      elif(order.order_type == "PickUp"):
        pass
      elif(order.order_type == "Delivery"):
        pass
      running = False
    elif(user_choice == "N"):
      running = False

    else:
      print("\n\nINVALID INPUT\n")

def proceed_dinein_checkout(order: DineIn):
  print("\n\nItemized Order:")
  print("FOOD")
  for food in order.get_products():
    print(food.get_product_details())
  print("DRINKS")
  for drink in order.get_drinks():
    print(drink.get_product_details())
  print("Dine in Charge (15% of the total order)", order.get_dinein_charge())
  print("------------------------------")
  print("TOTAL CHARGE.                          ", order.calculate_total_amount())

  orders.append(order)

def show_report(report_type):
    report_data = ""
    if (report_type == "1"):
        report_data = Order.get_order_summary(current_customer, "DineIn")

    elif (report_type == "2"):
        report_data = Order.get_order_summary(current_customer, "PickUp")

    elif (report_type == "3"):
        report_data = Order.get_order_summary(current_customer, "Delivery")

    elif (report_type == "4"):
        report_data = Order.get_order_summary(current_customer, "All")

    elif (report_type == "5"):
        report_data = Order.get_order_summary(current_customer, "Total")

    print()
    print(report_data)
## End update



"""# ------------------------------- Main Code Area -------------------------------

here we place the main executions and calls for the system
"""

# Main definitions

running = True

orders = []
current_customer = None
customers = [Customer("Charles", "0424355025", "Melbourne", "22/03/1990", "Gwapo@1")]

drinks = [Product("Coffee", 2, "Drink"), Product("Colddrink", 4, "Drink")]
drinks.append(Product("Shake", 6, "Drink"))

foods = [Product("Noodles", 2, "Food"), Product("Sandwitch", 4, "Food")]
foods.append(Product("Dumpling", 6, "Food"))
foods.append(Product("Muffins", 8, "Food"))
foods.append(Product("Pasta", 10, "Food"))
foods.append(Product("Pizza", 20, "Food"))

# Main loop

while(running):
  sel = top_menu()
  print()
  if(sel == "1"):
    function_selector(SIGN_UP)
  elif(sel == "2"):
    exists, customer = sign_in(customers)
    if(exists and not customer):
      print("The password you entered did not match...")
    elif(not exists):
      print("The mobile you entered does not exist in the database")
    elif(exists and customer):
      current_customer = customer
      print("You have successfully Signed in\n")
      function_selector(SIGN_IN)
  elif(sel == "3"):
    print("Goodbye...\n Have a nice day...")
    running = False
  else:
    print("You entered an invalid input selection...\nPlease enter again...\n")