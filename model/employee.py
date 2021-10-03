"""
Employee Model

Handles Getter/Settings, and the Data Model. Also handles a To-String (To-CSV?)
Function that the Repository code will use.

Properties
id: Employee IDs, Required
first_name: String, Required
last_name: String, Required
archived: Boolean, Required
social_security: String <###-##-###>, Required
title: String, Required
department: String, Required
office_email: String <john@email.com>, Required if no office_phone
office_phone: String <(###) ###-####>, Required if no office_email
start_date: String <MM/DD/YYYY>, Required
imported: Boolean, Required: Used to swap "Start Date" to "Imported Date" if needs be
street_address: String, Required
city: String, Required
state: String, Required
zipcode: String, Required, Can be Long Postal Code, or Shorten Zip code
classification: Int - Maps to Classification Enum, Required
payment_Method: Int - Maps to payment_Method Enum, Required
salary: Double - ANNUAL SALARY, Required FOR Salaried/Commissioned
rate: Double - Hourly/Commission, Required FOR Commisioned/Hourly

Employees are paid Bi-Monthly
Salaried Employees receive 1/24th of Annual Salary
Hourly Employees are paid Hourly Rate * Hour worked that bi month.
Commissioned Employees are Salaried + Commission Fees.
"""
from enums.classification import Classification
from enums.paycheck_method import Paycheck_Method
#Bonuses? Total/Received?
class Employee:
    #It would be easy to use **KWARGS here, but I want to be more explicit.
    def __init__(self, input_dictionary):
        self.id = input_dictionary["id"]
        self.first_name = input_dictionary["first_name"]
        self.last_name = input_dictionary["last_name"]
        self.archived = input_dictionary["archived"]
        self.social_security = input_dictionary["social_security"]
        self.title = input_dictionary["title"]
        self.department = input_dictionary["department"]
        self.office_email = input_dictionary["office_email"]
        self.office_phone = input_dictionary["office_phone"]
        self.start_date = input_dictionary["start_date"]
        self.imported = input_dictionary["imported"]
        self.street_address = input_dictionary["street_address"]
        self.city = input_dictionary["city"]
        self.state = input_dictionary["state"]
        self.zipcode = input_dictionary["zipcode"]
        #See the Enums Module for value reference.
        self.classification = int(input_dictionary["classification"])
        self.payment_Method = int(input_dictionary["payment_method"])
        self.salary = 0
        self.rate = 0
        self.route = input_dictionary["route"]
        self.account = input_dictionary["account"]
        self.valid = False

        self.set_income(input_dictionary["income"])
        self._validate()

    #We'll parse in this information, however we might want
    #to adjust this in case we want to quickly toggle employees
    #without inputting a payment value each time.
    def set_income(self, money):
        if self.classification == Classification.SALARIED.value:
            self.salary = money[0]
        if self.classification == Classification.HOURLY.value:
            self.rate = money[1]
        if self.classification == Classification.COMMISSIONED.value:
            self.salary = money[0]
            self.rate = money[2]

    #Private Method
    def __get_income(self):
        if self.classification == Classification.SALARIED.value:
            return self.salary
        if self.classification == Classification.HOURLY.value:
            return self.rate
        if self.classification == Classification.COMMISSIONED.value:
            return [self.salary, self.rate]

    #Wrapper for __get_income(), just to abstract out the logic.
    def get_pay(self):
        return [self.payment_Method, self.classification, self.__get_income()]

    #Apt Number?
    def get_address(self):
        return (self.street_address + " " + self.city + ", " + self.state + " "
                + self.zipcode)

    #EX James Bond
    def get_full_name(self):
        return (self.first_name + " " + self.last_name)

    #EX, Bond, James
    def get_reversed_name(self):
        return (self.last_name + ", " + self.first_name)

    def get_basic_info(self):
        return {
            "name" : self.get_full_name(),
            "id" : self.id,
            "department" : self.department,
            "title" : self.title,
            "email" : self.office_email,
            "phone" : self.office_phone
        }

    #Checks if all the fields are valid, we'll run this once at start, and then
    def _validate(self):
        pass

    #Potentially could be removed if we decided to use file.writeLines()
    #But this maintains current format.
    def save_format(self):
        base = ""
        property_value = self.__dict__.values()
        for value in property_value:
            if value == None:
                value = ""
            base += str(value) + ","
        return (base[:-1] + "\n")

    #Used if we need to print out the Employee to the Console.
    def __str__(self):
        base = ""
        property_value = self.__dict__.values()
        for value in property_value:
            base += str(value) + ","
        return (base[:-1])
