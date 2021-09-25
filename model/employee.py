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

Employees are paid Bi-Monthly
Salaried Employees receive 1/24th of Annual Salary
Hourly Employees are paid Hourly Rate * Hour worked that bi month.
Commissioned Employees are Salaried + Commission Fees.
"""
from enums.classification import Classification
from enums.paycheck_method import Paycheck_Method
#Bonuses? Total/Received?
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
        #See the Enums Module for value reference.
        self.classification = int(classification)
        self.payment_Method = int(payment_Method)
        self.salary = 0
        self.rate = 0
        self.route = route
        self.account = account

        self.set_income(income)

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

    #If we decide to store the name as First/Last, or we can convert this to split the name.
    #Basically a wrapper just to prevent unexpected behavior.
    def get_name(self):
        return self.name

    #Potentially could be removed if we decided to use file.writeLines()
    #But this maintains current format.
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
               +str(self.rate) + ","
               +str(self.route) + ","
               +str(self.account) + "\n")

    #Used if we need to print out the Employee to the Console.
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
               +str(self.rate) + ","
               +str(self.route) + ","
               +str(self.account))
