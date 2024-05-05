# ------ Imports --------------------------------------------------------------------
# here we place the libraries we are importing
import datetime
import random
import re
# ----- Global variables area --------------------------------------------------------
# here we place variables that are visible throughout the whole program
# Var to store all the customer selection
items_selection = []

user_login = [] # list that will store all the customer data
customer_master_list = []


# -----------------------------------------------------------------------------------

# --------------------- Area for Class Definition ------------------------
# here we place different class definitions we may be using
# ---- parent class is Person Class  ----
class Product:
    # Creating the menu list for Food and Drink to reduce the amount of code.
    # The products will be already loaded on the system.

    drinkD = ['Coffee', 'Colddrink', 'Shake ', 'for Checkout']
    drinkP = [2, 4, 6]

    foodD = ['Noodles', 'Sandwich', 'Dumpling', 'Muffins', 'Pasta   ', 'Pizza    ', 'for Drinks Menu:']
    foodP = [2, 4, 6, 8, 10, 20]
    count = 1

    # ----------------- Initialser/constructor area
    # def __init__(self):
    #     pass

    # ----------------- method area
    def display_items_selection(self):
        # for i in items_selection:
        #     print(i)
        print(items_selection)
    def display_food_menu(self):
        #i = 0
        print("--------- Food Menu Choices --------\n")

        for i in range(len(Product.foodD)):
            if i < 6:
                print("Enter ", Product.count, Product.foodD[i], "\t \t Price AUD ", Product.foodP[i])
                Product.count += 1
            else:
                print("Enter ", Product.count, Product.foodD[i])

    def select_food_menu(self, select_items):

        if select_items <= 0 or select_items > 7:
            print("Invalid Option")
        elif select_items == 1:
            # print(Product.foodD[0], Product.foodP[0])
            order = [Product.foodD[0], Product.foodP[0]]
            items_selection.append(order)
            # user_login.append(items_selection)
            # user_login.append(items_selection.append(order))
        elif select_items == 2:
            order = [Product.foodD[1], Product.foodP[1]]
            items_selection.append(order)
        elif select_items == 3:
            order = [Product.foodD[2], Product.foodP[2]]
            items_selection.append(order)
        elif select_items == 4:
            order = [Product.foodD[3], Product.foodP[3]]
            items_selection.append(order)
        elif select_items == 5:
            order = [Product.foodD[4], Product.foodP[4]]
            items_selection.append(order)
        elif select_items == 6:
            order = [Product.foodD[5], Product.foodP[5]]
            items_selection.append(order)



    def display_drink_menu(self):
        Product.count = 1
        print("--------- Drink Menu Choices --------\n")
        for i in range(len(Product.drinkD)):
            if i < 3:
                print("Enter ", Product.count, self.drinkD[i], "\t \t Price AUD ", self.drinkP[i])
                Product.count += 1
            else:
                print("Enter ", Product.count, Product.drinkD[i])

    def select_drink_menu(self, select_items):

        if select_items <= 0 or select_items > 4:
            print("Invalid Option")
        elif select_items == 1:
            # print(Product.foodD[0], Product.foodP[0])
            order = [Product.drinkD[0], Product.drinkP[0]]
            items_selection.append(order)
        elif select_items == 2:
            order = [Product.drinkD[1], Product.drinkP[1]]
            items_selection.append(order)
        elif select_items == 3:
            order = [Product.drinkD[2], Product.drinkP[2]]
            items_selection.append(order)
        elif select_items == 4:
            order = [Product.drinkD[3], Product.drinkP[3]]
            items_selection.append(order)

class Customer:

    # ----------------- method area
    
    def __init__(self):
        proceed = True
        
        print("\n----- Customer Registration -----\n")
        name = input("Name".ljust(27, " ") + ": ")
        mobile_number = input("Mobile Number".ljust(27, " ") + ": ")
        date_of_birth = input("Date of Birth (DD/MM/YYYY)"
                                       .ljust(27, " ") + ": ")
        address = input("Address".ljust(27, " ") + ": ")
        password = input("Password".ljust(27, " ") + ": ")
        confirm_password = input("Confirm Password"
                                          .ljust(27, " ") + ": ")
            
        ## Name Validation
        nameRegexPattern = "^[A-Za-z\-\_]{1,35}(\s[A-Za-z]{0,35})?$"
        match = re.search(nameRegexPattern, name)
        if not match:
            proceed = False
            print("\nIncorrect name pattern. Names should only be alphabets, - or _.")

        ## Mobile Validate
        mobileRegexPattern = "^[0-9]{10}$"
        match = re.search(mobileRegexPattern, mobile_number) 
        if match:
            for customer in customer_master_list:
                if(customer.mobile_number == mobile_number):
                    print ("\nMobile Number already exists!. Please try again.")
                    proceed = False
                    break            
        else:
            proceed = False
            print("\nPlease enter 10 digit mobile number starting with 0.")
            
        ## DOB Validation
        dobRegexPattern = "^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[1,2])/(19|20)[0-9]{2}$"
        match = re.search(dobRegexPattern, date_of_birth) 
        if match:
            if ((int(date_of_birth[6:]) % 4 == 0 and int(date_of_birth[6:]) % 100 != 0)
                or int(date_of_birth[6:]) % 400 == 0):
                dobLeapRegexPattern = "^(0[1-9]|[12][0-9])/(0[1-9]|1[1,2])/(19|20)[0-9]{2}$"
                match = re.search(dobLeapRegexPattern, date_of_birth)
                if not match:
                    proceed = False
                    print("\nPlease enter date in format dd/mm/yyyy.")
        else:
            proceed = False
            print("\nPlease enter date in format dd/mm/yyyy.")
            
        ## Password Validation
        if password == confirm_password:
            passwordRegexPattern = "^[a-zA-Z]*[@|&|#][0-9]*$"
            match = re.search(passwordRegexPattern, password)
            if not match:
                proceed = False
                print("\nIncorrect password pattern. Password should start with "\
                      "alphabet followed by @, & or # and ends with numbers.")
        else:
            proceed = False
            print("\nYour passwords are not matching.\n"\
                      "Please try again.\n")
                
        if proceed == True:
            # Update --------
            self.__id = len(customer_master_list) + 1
            self.name = name
            self.mobile_number = mobile_number
            self.date_of_birth = date_of_birth
            self.password = password
            self.address = address
        else:
            # Update ---------
            self.__id = 0
            
    ## Update -----------
    def get_id(self):
        return self.__id
        
    def show_customer_details(self):
        print(f"Thank you, {self.customerName} your id , {self.customerMobile}")
        #user_data = [self.customerName,  self.customerAddress, self.customerMobile, self.customerDBO, self.customerPas1, self.customerPas2]
        #user_login.append(user_data)
        #for i in user_login:
         #   print(i)

class Order(Customer):
    orderID = ''
    totalOrder_amount = 0


    def __init__(self, customerMobile, customerName):
        self.customerMobile = customerMobile
        self.customerName = customerName

    # This method will create a customer history
    def print_Order(self):
        # Building a unique order code
        #pre-fix "OID" + first 3 number of the customer mobile + first wto letter of the customer name
        self.orderID = 'OID' + self.customerMobile[:3] + self.customerName[:2]

        user_login.append(self.orderID)
        user_login.append(self.customerMobile)
        user_login.append(items_selection)

        for i in items_selection:
             self.totalOrder_amount += i[1]

        amount = "Order Amount: $", self.totalOrder_amount
        user_login.append(amount)
        print("User data: ", user_login)



# Test of classes
class Dine_In(Customer):

    order_type = 1
    numberCustomer = 0
    dateVisit = ""
    timeVisit = ""

    def __init__(self, get_id):
        self.id = get_id

    def display_dine_in_customer(self):
        print(self.get_id())

    def dineIn_futher_detials(self):
        print("-------- Dine-In details ---------")
        Dine_In.numberCustomer = int(input("Enter number of customer: "))
        Dine_In.dateVisit = input("Enter date of visit: ")
        Dine_In.timeVisit = input("Enter time of visit: ")

class Pick_Up:

    order_type = 2
    nameCustomer = 0
    datePickup = ""
    timePickup = ""
    unique_code_order = 0

    def __init__(self, customerMobile):
        self.customerMobile = customerMobile

    def pickUp_unique_code(self):

        unique_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.unique_code_order = "B" + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers))
        return self.unique_code_order


    def pickUp_futher_detials(self):
        print("-------- Pick-Up detials ---------")
        Pick_Up.nameCustomer = input("Enter name of customer: ")
        Pick_Up.datePickup = input("Enter date of pick up: ")
        Pick_Up.timePickup = input("Enter time of pick up: ")

        # Creating a validtion condition to check each input from the user

        # Printing message
        print("Thank You for entering the details, Your Booking is confirmed.")
        print("Order confirmation code: ", self.pickUp_unique_code())

class Delivery():

    order_type = 3
    distanceDely = 0
    dateDely = ""
    timeDely = ""
    unique_code_order = 0

    def __init__(self, customerMobile):
        self.customerMobile = customerMobile

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
        print(self.customerMobile)
        print(self.distanceDely)
        print(self.dateDely)
        print(self.timeDely)
        print(self.delivery_unique_code())


# -------------- Function Area ------------------------------------------
# here we place definitions for general functions

def app_menu() -> int:
    print("B2B Restaurant Mobile Application")
    print("[1] Sign Up")
    print("[2] Sign In")
    print("[3] Quit Application")
    user_choice = input("Please enter your choice: ")

    return user_choice

def app_signIn_menu() -> int:
    print("[1] Start Ordering. ")
    print("[2] Print Statistics. ")
    print("[3] Logout. ")
    user_choice = input("Please enter your choice: ")

    return user_choice

def app_ordering_menu() -> int:
    print("[1] Dine in. ")
    print("[2] Order Online. ")
    print("[3] Login Page. ")
    user_choice = input("Please enter your choice: ")

    return user_choice

def app_Order_online_menu() -> int:
    print("[1] Self Pickup. ")
    print("[2] Home Delivery. ")
    print("[3] Previous Menu. ")
    user_choice = input("Please enter your choice: ")

    return user_choice
def app_summary_transactions() -> int:
    print("Please Enter the Option to Print the Statistics.")
    print("[1] All Dine in Orders. ")
    print("[2] All Pick up Orders. ")
    print("[3] All Delivery Orders. ")
    print("[4] All Orders. (Ascending Order)")
    print("[5] Total Amount Spent on All Orders. ")
    print("[6] To go to Previous Menu. ")

    user_choice = input("Please enter your choice: ")

    return  user_choice

# main Area code -----------------------------------


# testing customer initialization
#customerName, customeMobile, customerAddress, customerDBO, customerPas1, customerPas2
# c1 = Customer('wellington', '0406397823','38 Mt Alexander Road','10/05/1994','wel@1234','wel@1234')
#c1.show_customer_details()

c1 = Customer()

print('\n')
print(c1.get_id())
#
# d1 = Dine_In(c1.get_id())
#
# d1.dineIn_futher_detials()


#
# # Testing classes type-order
# d1 = Dine_In(c1.customerMobile)
# d1.dineIn_futher_detials()
#
# p1 = Pick_Up(c1.customerMobile)
# p1.pickUp_futher_detials()
# p1.pickUp_unique_code()

# de = Delivery(c1.customerMobile)
# de.delivery_further_details()






# Calling the menus options
# app_menu()
# app_signIn_menu()
# app_ordering_menu()
# app_Order_online_menu()


#calling the object product and its methods for display and select items
# prd = Product()
# prd.display_food_menu()
#
# while True:
#     user_selection = int(input("Enter your choice: "))
#     if user_selection == 7:
#         break
#     prd.select_food_menu(user_selection)
#
# prd.display_drink_menu()
# while True:
#     user_selection = int(input("Enter your choice: "))
#     if user_selection == 4:
#         break
#     prd.select_drink_menu(user_selection)
#
#
# orderb1 = Order(c1.customerMobile, c1.customerName)
# orderb1.print_Order()
#
# app_summary_transactions()

# prd.display_items_selection()
# c1.show_customer_details()


#
# test_amount = [['Noodles', 2], ['Noodles', 2], ['Noodles', 2], ['Noodles', 2]]
#
# for i in test_amount:
#     print(i[1])