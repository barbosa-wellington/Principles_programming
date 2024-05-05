# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:20:34 2024

@author: William
"""
## Imports
from datetime import datetime

## Global Variables
product_list = []
order_list = []

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__type = ""
    
    def set_type(self, type):
        self.__type = type
        
    def get_type(self):
        return self.__type
    
class Food(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.set_type("Food")
        
class Beverage(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.set_type("Beverage")















class Order:
    def __init__(self, customer_id):
        self.__customer_id = customer_id
        self.__id = len(order_list) + 1
        self.__type = ""
        self.__product_list = []
    
    def set_type(self, type):
        self._type = type
        
    def get_type(self):
        return self._type
    
    def get_id(self):
        return self.__id
          
    def add_product(self, product, quantity):
        self.new_product = []
        self.new_product.append(product)
        self.new_product.append(quantity)
        self.__product_list.append(self.new_product)
    
    def show_order_confirmation(self):
        print("Thank you for entering the details, Your booking is confirmed.")
        print("Your transaction number is B"+str(self.__id).zfill(3))
        
    def confirm_order(self):
        self._date = datetime.today().strftime("%d/%m/%Y")
        self._time = datetime.now().time().strftime("%H:%M")
        order_list.append(self)
        
        
class Dine_In(Order):
    def __init__(self, customer_id):
        super().__init__(customer_id)
        self.set_type("Dine In")
        
    def add_further_details(self, no_of_persons, date_of_visit, time_of_visit):
        self.no_of_persons = no_of_persons
        self.date_of_visit = date_of_visit
        self.time_of_visit = time_of_visit
        
class Pick_Up(Order):
    def __init__(self, customer_id):
        super().__init__(customer_id)
        self.set_type("Pick Up")
    
    def add_further_details(self, date_of_pickup, time_of_pickup,
                            name_of_pickup_person):
        self.date_of_pickup = date_of_pickup
        self.time_of_pickup = time_of_pickup
        self.name_of_pickup_person = name_of_pickup_person
        
class Delivery(Order):
    def __init__(self, customer_id):
        super().__init__(customer_id)
        self.set_type("Delivery")
    
    def add_further_details(self, date_of_delivery, time_of_delivery, distance):
        self.date_of_delivery = date_of_delivery
        self.time_of_delivery = time_of_delivery
        self.distance = distance
        
    def show_order_confirmation(self):
        print("Thank you for your Order, Your Order has been confirmed.")
        print("Your transaction number is B"+str(self.get_id()).zfill(3))
        
## Create Product List
product_list.append(Food("Noodles",2))
product_list.append(Food("Sandwich",4))
product_list.append(Food("Dumpling",6))
product_list.append(Food("Muffins",8))
product_list.append(Food("Pasta",10))
product_list.append(Food("Pizza",20))
product_list.append(Beverage("Coffee",2))
product_list.append(Beverage("Cold Drink",4))
product_list.append(Beverage("Shake",6))

# Testing
date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%H:%M")
o1 = Dine_In(1)
o1.add_product(product_list[0], 1)
o1.add_further_details(1, date, time)
o1.confirm_order()
o1.show_order_confirmation()

date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%H:%M")
o2 = Pick_Up(2)
o2.add_product(product_list[2], 1)
o2.add_product(product_list[3], 2)
o2.add_further_details(date, time, "William")
o2.confirm_order()
o2.show_order_confirmation()

date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%H:%M")
o3 = Delivery(3)
o3.add_product(product_list[4], 1)
o3.add_product(product_list[5], 2)
o3.add_further_details(date, time, 2)
o3.confirm_order()
o3.show_order_confirmation()

# End of Testing

            
        
        