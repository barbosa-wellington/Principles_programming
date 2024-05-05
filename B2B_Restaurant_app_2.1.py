# # ------ Imports --------------------------------------------------------------------
# # here we place the libraries we are importing
# import datetime
# import random
# import re
# # ----- Global variables area --------------------------------------------------------
# # here we place variables that are visible throughout the whole program
# # Var to store all the customer selection
# items_selection = []

# user_login = [] # list that will store all the customer data
# customer_master_list = []


# # -----------------------------------------------------------------------------------

# # --------------------- Area for Class Definition ------------------------
# # here we place different class definitions we may be using
# # ---- parent class is Person Class  ----
# class Product:
#     # Creating the menu list for Food and Drink to reduce the amount of code.
#     # The products will be already loaded on the system.

#     drinkD = ['Coffee', 'Colddrink', 'Shake ', 'for Checkout']
#     drinkP = [2, 4, 6]

#     foodD = ['Noodles', 'Sandwich', 'Dumpling', 'Muffins', 'Pasta   ', 'Pizza    ', 'for Drinks Menu:']
#     foodP = [2, 4, 6, 8, 10, 20]
#     count = 1

#     # ----------------- Initialser/constructor area
#     # def __init__(self):
#     #     pass

#     # ----------------- method area

#     def display_food_menu(self):
#         #i = 0
#         print("--------- Food Menu Choices --------\n")

#         for i in range(len(Product.foodD)):
#             if i < 6:
#                 print("Enter ", Product.count, Product.foodD[i], "\t \t Price AUD ", Product.foodP[i])
#                 Product.count += 1
#             else:
#                 print("Enter ", Product.count, Product.foodD[i])
#     def select_food_menu(self, select_items):


#         if 1 <= select_items <= len(self.foodD):
#             order = [Product.foodD[select_items -1], Product.foodP[select_items -1]]
#             items_selection.append(order)
#         else:
#             print("Invalid Food item")
#     def display_drink_menu(self):
#         Product.count = 1
#         print("--------- Drink Menu Choices --------\n")
#         for i in range(len(Product.drinkD)):
#             if i < 3:
#                 print("Enter ", Product.count, self.drinkD[i], "\t \t Price AUD ", self.drinkP[i])
#                 Product.count += 1
#             else:
#                 print("Enter ", Product.count, Product.drinkD[i])
#     def select_drink_menu(self, select_items):

#         if 1 <= select_items <= len(self.drinkD):
#             order = [Product.drinkD[select_items -1], Product.drinkP[select_items - 1]]
#             items_selection.append(order)
#         else:
#             print("Invalid Drink item")
#     def display_items_selection(self):
#         # for i in items_selection:
#         #     print(i)
#         print(items_selection)

# class Customer:

#     def __init__(self, customerName, customeMobile, customerAddress, customerDBO, customerPas1, customerPas2):
#         self.__id = len(customer_master_list) + 1
#         self.customerName = customerName
#         self.customerMobile = customeMobile
#         self.customerAddress = customerAddress
#         self.customerDBO = customerDBO
#         self.customerPas1 = customerPas1
#         self.customerPas2 = customerPas2

#     # # ----------------- Initialser/constructor area
#     # # def __init__(self):
#     # #     pass

#     # # ----------------- method area

#     def get_customer_data(self):

#         return self.customerName, self.customerMobile, self.customerAddress, self.customerDBO, self.customerPas1,self.customerPas2

#     def updating_user_loging_date(self):

#         user_data = [self.__id, self.customerName, self.customerAddress, self.customerMobile, self.customerDBO, self.customerPas1, self.customerPas2]
#         user_login.append(user_data)
#         customer_master_list.append(customer_master_list)

#     def get_id(self):
#         return self.__id

#     def show_customer_details(self):

#         for i in user_login:
#             print(i)

# class Order:
#     orderID = ''
#     totalOrder_amount = 0


#     def __init__(self, id, customerMobile, orderType, date):
#         self.id = id
#         self.customerMobile = customerMobile
#         self.orderType = orderType
#         self.date = date


#     def display_order_info(self):

#         print(user_login)

#     def order_id_generate(self):

#         unique_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#         self.orderID = "OID" + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers))
#         return self.orderID

#     # This method will create a customer history
#     def create_order_data(self):

#         user_login.append(self.order_id_generate())
#         # user_login.append(self.customerMobile)
#         # user_login.append(items_selection)
#         user_login.append(self.date)


#         for i in items_selection:
#              self.totalOrder_amount += i[1]

#         amount = self.totalOrder_amount
#         user_login.append(amount)
#         user_login.append(self.orderType)



# class Dine_In:

#     order_type = "dine-in"
#     numberCustomer = 0
#     dateVisit = ""
#     timeVisit = ""
#     dineIn_fee = 0.15

#     def __init__(self, id):
#         self.id = id

#     def display_dine_in_customer(self):
#         print("Customer ID", self.id)

#     def dineIn_futher_detials(self):
#         print("-------- Dine-In details ---------")
#         Dine_In.numberCustomer = int(input("Enter number of customer: "))
#         Dine_In.dateVisit = input("Enter date of visit: ")
#         Dine_In.timeVisit = input("Enter time of visit: ")


#         print("Thank You for entering the details, Your Booking is confirmed.")

# class Pick_Up:

#     order_type = "pick-up"
#     nameCustomer = 0
#     datePickup = ""
#     timePickup = ""
#     unique_code_order = 0

#     def __init__(self, id):
#         self.id = id

#     def pickUp_unique_code(self):

#         unique_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#         self.unique_code_order = "B" + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers))
#         return self.unique_code_order


#     def pickUp_futher_detials(self):
#         print("-------- Pick-Up detials ---------")
#         Pick_Up.nameCustomer = input("Enter name of customer: ")
#         Pick_Up.datePickup = input("Enter date of pick up: ")
#         Pick_Up.timePickup = input("Enter time of pick up: ")

#         # Printing message
#         print("Thank You for entering the details, Your Booking is confirmed.")
#         print("Order confirmation code: ", self.pickUp_unique_code())

# class Delivery:

#     order_type = "delivery"
#     distanceDely = 0
#     dateDely = ""
#     timeDely = ""
#     unique_code_order = 0

#     def __init__(self, id):
#         self.id = id

#     def delivery_distance_calculation(self):

#         if (Delivery.distanceDely >= 0 and Delivery.distanceDely <= 4):
#             print(" Delivery charge will be 3$.")
#         elif (Delivery.distanceDely > 4 and Delivery.distanceDely <= 8):
#             print(" Delivery charge will be 6$.")
#         elif (Delivery.distanceDely > 8 and Delivery.distanceDely <= 12):
#             print(" Delivery charge will be 10$.")
#         elif (Delivery.distanceDely > 12):
#             print(" No delivery can be done.")

# # Unique code method generate
#     def delivery_unique_code(self):

#         unique_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#         self.unique_code_order = "B" + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers))
#         return self.unique_code_order

#     def delivery_further_details(self):

#         print("-------- Delivery details ---------")
#         Delivery.distanceDely = int(input("Enter the distance in KM: "))
#         Delivery.delivery_distance_calculation(self.distanceDely)
#         Delivery.dateDely = input("Enter delivery date: ")
#         Delivery.timeDely = input("Enter delivery time: ")

#         #Creating a validtion condition to check each input from the user

#         #Printing message
#         print("Thank You for entering the details, Your Booking is confirmed.")
#         print("Order confirmation code: ", self.delivery_unique_code())

#     def display_delivery_customer(self):
#         print(self.id)
#         print(self.distanceDely)
#         print(self.dateDely)
#         print(self.timeDely)
#         print(self.delivery_unique_code())


# # -------------- Function Area ------------------------------------------
# # here we place definitions for general functions

# def app_menu() -> int:
#     print("B2B Restaurant Mobile Application")
#     print("[1] Sign Up")
#     print("[2] Sign In")
#     print("[3] Quit Application")
#     user_choice = input("Please enter your choice: ")

#     return user_choice

# def app_signIn_menu() -> int:
#     print("[1] Start Ordering. ")
#     print("[2] Print Statistics. ")
#     print("[3] Logout. ")
#     user_choice = input("Please enter your choice: ")

#     return user_choice

# def app_ordering_menu() -> int:
#     print("[1] Dine in. ")
#     print("[2] Order Online. ")
#     print("[3] Login Page. ")
#     user_choice = input("Please enter your choice: ")

#     return user_choice

# def app_Order_online_menu() -> int:
#     print("[1] Self Pickup. ")
#     print("[2] Home Delivery. ")
#     print("[3] Previous Menu. ")
#     user_choice = input("Please enter your choice: ")

#     return user_choice
# def app_summary_transactions() -> int:
#     print("Please Enter the Option to Print the Statistics.")
#     print("[1] All Dine in Orders. ")
#     print("[2] All Pick up Orders. ")
#     print("[3] All Delivery Orders. ")
#     print("[4] All Orders. (Ascending Order)")
#     print("[5] Total Amount Spent on All Orders. ")
#     print("[6] To go to Previous Menu. ")

#     user_choice = input("Please enter your choice: ")

#     return  user_choice

# # main Area code -----------------------------------

# # Thank You for entering the details, Your Booking is confirmed.
# # Order confirmation code:  B413

# # User data:  ['OID0981', '0987876789', 'delivery', ('Order Amount: $', 58)]





# def restaurant_app_main():
#     while True:
#         choice = app_menu()

#         # Start the signup options
#         if choice == '1':
#             print("Signing up....")

#             proceed = True

#             print("\n----- Customer Registration -----\n")
#             name = input("Name".ljust(27, " ") + ": ")
#             mobile_number = input("Mobile Number".ljust(27, " ") + ": ")
#             date_of_birth = input("Date of Birth (DD/MM/YYYY)"
#                                   .ljust(27, " ") + ": ")
#             address = input("Address".ljust(27, " ") + ": ")
#             password = input("Password".ljust(27, " ") + ": ")
#             confirm_password = input("Confirm Password"
#                                      .ljust(27, " ") + ": ")

#             ## Name Validation
#             nameRegexPattern = "^[A-Za-z\-\_]{1,35}(\s[A-Za-z]{0,35})?$"
#             match = re.search(nameRegexPattern, name)
#             if not match:
#                 proceed = False
#                 print("\nIncorrect name pattern. Names should only be alphabets, - or _.")

#             ## Mobile Validate
#             mobileRegexPattern = "^[0-9]{10}$"
#             match = re.search(mobileRegexPattern, mobile_number)
#             if match:
#                 for customer in customer_master_list:
#                     if (customer.mobile_number == mobile_number):
#                         print("\nMobile Number already exists!. Please try again.")
#                         proceed = False
#                         break
#             else:
#                 proceed = False
#                 print("\nPlease enter 10 digit mobile number starting with 0.")

#             ## DOB Validation
#             dobRegexPattern = "^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[1,2])/(19|20)[0-9]{2}$"
#             match = re.search(dobRegexPattern, date_of_birth)
#             if match:
#                 if ((int(date_of_birth[6:]) % 4 == 0 and int(date_of_birth[6:]) % 100 != 0)
#                         or int(date_of_birth[6:]) % 400 == 0):
#                     dobLeapRegexPattern = "^(0[1-9]|[12][0-9])/(0[1-9]|1[1,2])/(19|20)[0-9]{2}$"
#                     match = re.search(dobLeapRegexPattern, date_of_birth)
#                     if not match:
#                         proceed = False
#                         print("\nPlease enter date in format dd/mm/yyyy.")
#             else:
#                 proceed = False
#                 print("\nPlease enter date in format dd/mm/yyyy.")

#             ## Password Validation
#             if password == confirm_password:
#                 passwordRegexPattern = "^[a-zA-Z]*[@|&|#][0-9]*$"
#                 match = re.search(passwordRegexPattern, password)
#                 if not match:
#                     proceed = False
#                     print("\nIncorrect password pattern. Password should start with alphabet followed by @, & or # and ends with numbers.")
#             else:
#                 proceed = False
#                 print("\nYour passwords are not matching.\n" \
#                       "Please try again.\n")


#             if (name != None) and (mobile_number != None) and (date_of_birth != None) and (password != None) and (confirm_password != None):
#                 c1 = Customer(name, mobile_number, address, date_of_birth, password, confirm_password)
#                 c1.updating_user_loging_date()

#                 print("You have Successfully Signed up.")
#                 continue
#                 app_menu()
#             else:
#                 print("check all the information again")

#         # Creating the validation
#         elif choice == '2':
#             print("Signing in....")
#             print("validating the customer phone number na password...")
#         elif choice == '3':
#             print("Exiting the application")
#             quit()
#         else:
#             print("Invalid input...")

#         while True:
#             choice = app_signIn_menu()

#             if choice == '1':
#                 print("Ordering selection")
#             elif choice == '2':

#                 # This will display the current customer data
#                 print("Printing customer statistics.")
#                 # It must call the app_menu_summary_transactions
#                 c1.show_customer_details()
#                 for i in items_selection:
#                     print(i)
#             elif choice == '3':
#                 app_menu()
#             else:
#                 print("Invalid option selected..")

#             while True:
#                 choice = app_ordering_menu()

#                 if choice == '1':
#                     print("Dine in selection option...")

#                     pd = Product()
#                     pd.display_food_menu()

#                     while True:
#                         user_selection = int(input("Enter your choice: "))
#                         if user_selection == 7:
#                             break
#                         pd.select_food_menu(user_selection)

#                     pd.display_drink_menu()
#                     while True:
#                         user_selection = int(input("Enter your choice: "))
#                         if user_selection == 4:
#                             break
#                         pd.select_drink_menu(user_selection)

#                     print(items_selection)

#                     dinein = Dine_In(c1.get_id())

#                     # print(dinein.order_type)
#                     dinein.dineIn_futher_detials()
#                     order_date =datetime.datetime.today().strftime("%d/%m/%Y")
#                     ord1 = Order(c1.get_id(), c1.customerMobile, dinein.order_type, order_date)
#                     ord1.create_order_data()
#                     ord1.display_order_info()


#                     break
#                     # Send the customer back to the login menu
#                     app_signIn_menu()
#                 elif choice == '2':
#                     print("Online options...")
#                     app_Order_online_menu()
#                 elif choice == '3':
#                     print("send to the login page...")
#                     app_signIn_menu()
#                 else:
#                     print("Invalid option pressed....")

#                 while True:
#                     choice = app_Order_online_menu()

#                     if choice == '1':
#                         print("This is the Pick-UP selections....")

#                         pd.display_food_menu()

#                         while True:
#                             user_selection = int(input("Enter your choice: "))
#                             if user_selection == 7:
#                                 break
#                             pd.select_food_menu(user_selection)

#                         print(items_selection)

#                         pickup = Pick_Up(c1.get_id())
#                         pickup.pickUp_futher_detials()

#                         order_date =datetime.datetime.today().strftime("%d/%m/%Y")
#                         ord2 = Order(c1.get_id(), c1.customerMobile, pickup.order_type, order_date)
#                         ord2.create_order_data()
#                         ord2.display_order_info()

#                         # Result test
#                         # 'OID0401', datetime.date(2024, 5, 4), ('Order Amount: $', 6), 'dine-in',
#                         # 'OID0401', datetime.date(2024, 5, 4), ('Order Amount: $', 18), 'pick-up']

#                         break
#                         # Send the customer back to the login menu
#                         app_signIn_menu()

#                     elif choice == '2':

#                         print("This is the Delivery selections....")
#                         pd = Product()
#                         pd.display_food_menu()

#                         while True:
#                             user_selection = int(input("Enter your choice: "))
#                             if user_selection == 7:
#                                 break
#                             pd.select_food_menu(user_selection)

#                         print(items_selection)

#                         delivery = Delivery(c1.get_id())
#                         delivery.delivery_further_details()

#                         order_date =datetime.datetime.today().strftime("%d/%m/%Y")
#                         ord3 = Order(c1.get_id(), c1.customerMobile, delivery.order_type, order_date)
#                         ord3.create_order_data()
#                         ord3.display_order_info()

#                         break
#                         # Send the customer back to the login menu
#                         app_signIn_menu()

#                     elif choice == '3':
#                         app_ordering_menu()
#                     else:
#                         print("Invalid option pressed...")







# # Initializing the application
# if __name__ == '__main__':
#     restaurant_app_main()
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


        if 1 <= select_items <= len(self.foodD):
            order = [Product.foodD[select_items -1], Product.foodP[select_items -1]]
            items_selection.append(order)
        else:
            print("Invalid Food item")
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

        if 1 <= select_items <= len(self.drinkD):
            order = [Product.drinkD[select_items -1], Product.drinkP[select_items - 1]]
            items_selection.append(order)
        else:
            print("Invalid Drink item")
    def display_items_selection(self):
        # for i in items_selection:
        #     print(i)
        print(items_selection)

class Customer:

    def __init__(self, customerName, customeMobile, customerAddress, customerDBO, customerPas1, customerPas2):
        self.__id = len(customer_master_list) + 1
        self.customerName = customerName
        self.customerMobile = customeMobile
        self.customerAddress = customerAddress
        self.customerDBO = customerDBO
        self.customerPas1 = customerPas1
        self.customerPas2 = customerPas2

    # # ----------------- Initialser/constructor area
    # # def __init__(self):
    # #     pass

    # # ----------------- method area

    def get_customer_data(self):

        return self.customerName, self.customerMobile, self.customerAddress, self.customerDBO, self.customerPas1,self.customerPas2

    def updating_user_loging_date(self):

        user_data = [self.__id, self.customerName, self.customerAddress, self.customerMobile, self.customerDBO, self.customerPas1, self.customerPas2]
        user_login.append(user_data)
        customer_master_list.append(customer_master_list)

    def get_id(self):
        return self.__id

    def show_customer_details(self):

        for i in user_login:
            print(i)

class Order:
    orderID = ''
    totalOrder_amount = 0


    def __init__(self, id, customerMobile, orderType, date):
        self.id = id
        self.customerMobile = customerMobile
        self.orderType = orderType
        self.date = date


    def display_order_info(self):

        print(user_login)

    def order_id_generate(self):

        unique_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.orderID = "OID" + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers)) + str(random.choice(unique_numbers))
        return self.orderID

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



class Dine_In:

    order_type = "dine-in"
    numberCustomer = 0
    dateVisit = ""
    timeVisit = ""
    dineIn_fee = 0.15

    def __init__(self, id):
        self.id = id

    def display_dine_in_customer(self):
        print("Customer ID", self.id)

    def dineIn_futher_detials(self):
        print("-------- Dine-In details ---------")
        Dine_In.numberCustomer = int(input("Enter number of customer: "))
        Dine_In.dateVisit = input("Enter date of visit: ")
        Dine_In.timeVisit = input("Enter time of visit: ")


        print("Thank You for entering the details, Your Booking is confirmed.")

class Pick_Up:

    order_type = "pick-up"
    nameCustomer = 0
    datePickup = ""
    timePickup = ""
    unique_code_order = 0

    def __init__(self, id):
        self.id = id

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

class Delivery:

    order_type = "delivery"
    distanceDely = 0
    dateDely = ""
    timeDely = ""
    unique_code_order = 0

    def __init__(self, id):
        self.id = id

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


# -------------- Function Area ------------------------------------------
# here we place definitions for general functions
## William update - sign in function, returns customer object if user is found and return error message if not
def user_sign_in(username, password):
    for customer in customer_master_list:
        if customer.customerMobile == username:
            if customer.customerPas1 == password:
                return customer
            else:
                return "\nInvalid username or password!\n"
        else:
            return "\nUser account does not exist!\n"
        
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

# Thank You for entering the details, Your Booking is confirmed.
# Order confirmation code:  B413

# User data:  ['OID0981', '0987876789', 'delivery', ('Order Amount: $', 58)]





def restaurant_app_main():
    while True:
        choice = app_menu()

        # Start the signup options
        if choice == '1':
            print("Signing up....")

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
                    if (customer.mobile_number == mobile_number):
                        print("\nMobile Number already exists!. Please try again.")
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
                    print("\nIncorrect password pattern. Password should start with alphabet followed by @, & or # and ends with numbers.")
            else:
                proceed = False
                print("\nYour passwords are not matching.\n" \
                      "Please try again.\n")

    
            if (name != None) and (mobile_number != None) and (date_of_birth != None) and (password != None) and (confirm_password != None):
                c1 = Customer(name, mobile_number, address, date_of_birth, password, confirm_password)
                # c1.updating_user_loging_date()
                ## William - add new customer to list,
                ## had to comment the method call above because it does not store the new customer into the customer list
                customer_master_list.append(c1)
                print("You have Successfully Signed up.")
                continue
                app_menu()
            else:
                print("check all the information again")

        # Creating the validation
        elif choice == '2':
            username = input("\nPlease enter username: ")
            password = input("Please enter password: " )
            
            customer = user_sign_in(username, password)
            
            while (type(customer) == str):
                print(customer)
                username = input("\nPlease enter username: ")
                password = input("Please enter password: " )
                
                customer = user_sign_in(username, password)

            print("\nYou have successfully signed in!\n")
            # print("Signing in....")
            # print("validating the customer phone number na password...")
            
            
        elif choice == '3':
            print("Exiting the application")
            quit()
        else:
            print("Invalid input...")

        while True:
            choice = app_signIn_menu()

            if choice == '1':
                print("Ordering selection")
            elif choice == '2':

                # This will display the current customer data
                print("Printing customer statistics.")
                # It must call the app_menu_summary_transactions
                c1.show_customer_details()
                for i in items_selection:
                    print(i)
            elif choice == '3':
                app_menu()
            else:
                print("Invalid option selected..")

            while True:
                choice = app_ordering_menu()

                if choice == '1':
                    print("Dine in selection option...")

                    pd = Product()
                    pd.display_food_menu()

                    while True:
                        user_selection = int(input("Enter your choice: "))
                        if user_selection == 7:
                            break
                        pd.select_food_menu(user_selection)

                    pd.display_drink_menu()
                    while True:
                        user_selection = int(input("Enter your choice: "))
                        if user_selection == 4:
                            break
                        pd.select_drink_menu(user_selection)

                    print(items_selection)

                    dinein = Dine_In(c1.get_id())

                    # print(dinein.order_type)
                    dinein.dineIn_futher_detials()
                    order_date =datetime.datetime.today().strftime("%d/%m/%Y")
                    ord1 = Order(c1.get_id(), c1.customerMobile, dinein.order_type, order_date)
                    ord1.create_order_data()
                    ord1.display_order_info()


                    break
                    # Send the customer back to the login menu
                    app_signIn_menu()
                elif choice == '2':
                    print("Online options...")
                    app_Order_online_menu()
                elif choice == '3':
                    print("send to the login page...")
                    app_signIn_menu()
                else:
                    print("Invalid option pressed....")

                while True:
                    choice = app_Order_online_menu()

                    if choice == '1':
                        print("This is the Pick-UP selections....")

                        pd.display_food_menu()

                        while True:
                            user_selection = int(input("Enter your choice: "))
                            if user_selection == 7:
                                break
                            pd.select_food_menu(user_selection)

                        print(items_selection)

                        pickup = Pick_Up(c1.get_id())
                        pickup.pickUp_futher_detials()

                        order_date =datetime.datetime.today().strftime("%d/%m/%Y")
                        ord2 = Order(c1.get_id(), c1.customerMobile, pickup.order_type, order_date)
                        ord2.create_order_data()
                        ord2.display_order_info()

                        # Result test
                        # 'OID0401', datetime.date(2024, 5, 4), ('Order Amount: $', 6), 'dine-in',
                        # 'OID0401', datetime.date(2024, 5, 4), ('Order Amount: $', 18), 'pick-up']

                        break
                        # Send the customer back to the login menu
                        app_signIn_menu()

                    elif choice == '2':

                        print("This is the Delivery selections....")
                        pd = Product()
                        pd.display_food_menu()

                        while True:
                            user_selection = int(input("Enter your choice: "))
                            if user_selection == 7:
                                break
                            pd.select_food_menu(user_selection)

                        print(items_selection)

                        delivery = Delivery(c1.get_id())
                        delivery.delivery_further_details()

                        order_date =datetime.datetime.today().strftime("%d/%m/%Y")
                        ord3 = Order(c1.get_id(), c1.customerMobile, delivery.order_type, order_date)
                        ord3.create_order_data()
                        ord3.display_order_info()

                        break
                        # Send the customer back to the login menu
                        app_signIn_menu()

                    elif choice == '3':
                        app_ordering_menu()
                    else:
                        print("Invalid option pressed...")







# Initializing the application
if __name__ == '__main__':
    restaurant_app_main()
