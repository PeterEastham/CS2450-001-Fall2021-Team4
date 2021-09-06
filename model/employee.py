"""
Employee Model

Handles Getter/Settings, and the Data Model. Also handles a To-String (To-CSV?)
Function that the Repository code will use.

Properties
id: Employee IDs, Required
name: Required
street_address: Required
city: Required
state: Required
zipcode: Required
classification: Salaried/Commissioned/Hourly, Required
payment_Method: Direct Deposit/Mailed, Required
salary: ANNUAL SALARY, Required IF classification.SALARIED
hourly: Required IF classification.HOURLY
commission_rate: Required IF classification.COMMISSIONED
"""
from enums.classification import Classification
from enums.paycheck_method import Paycheck_Method

class Employee:
    '''develops a payroll program for a company'''
    def __init__(self, id, name, street_address, city,
                state, zipcode, classification, payment_Method,
                income, route, account):
        self.id = id
        self.name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = int(classification)
        self.payment_Method = int(payment_Method)
        #Research more into Income Handling
        self.salary = 0
        self.hourly = 0
        self.commission_rate = 0
        self.route = route
        self.account = account
        self.permissions = []

        self.set_income(income)

    def set_income(self, money):
        if self.classification == Classification.SALARIED:
            self.salary = money[0]
        if self.classification == Classification.HOURLY:
            self.hourly = money[1]
        if self.classification == Classification.COMMISSIONED:
            self.commission_rate == money[2]

    def __get_income(self):
        if self.classification == Classification.SALARIED:
            return self.salary
        if self.classification == Classification.HOURLY:
            return self.hourly
        if self.classification == Classification.COMMISSIONED:
            return self.commission_rate

    def get_pay(self):
        return [self.payment_Method, self.classification, self.__get_income()]

    def get_address(self):
        return (self.street_address + " " + self.city + ", " + self.state + " "
                + self.zipcode)

    def get_name(self):
        return self.name

    def save_format(self):
        return (str(self.id) + ","
               +str(self.name) + ","
               +str(self.street_address) + ","
               +str(self.city) + ","
               +str(self.state) + ","
               +str(self.zipcode) + ","
               +str(self.classification) + ","
               +str(self.payment_Method) + ","
               +str(self.salary) + ","
               +str(self.hourly) + ","
               +str(self.commission_rate) + ","
               +str(self.route) + ","
               +str(self.account) + "\n")

    def __str__(self):
        return (str(self.id) + ","
               +str(self.name) + ","
               +str(self.street_address) + ","
               +str(self.city) + ","
               +str(self.state) + ","
               +str(self.zipcode) + ","
               +str(self.classification) + ","
               +str(self.payment_Method) + ","
               +str(self.salary) + ","
               +str(self.hourly) + ","
               +str(self.commission_rate) + ","
               +str(self.route) + ","
               +str(self.account))
