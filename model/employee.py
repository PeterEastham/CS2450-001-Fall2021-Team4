"""
Employee Model

Handles Getter/Settings, and the Data Model. Also handles a To-String (To-CSV?)
Function that the Repository code will use.
"""
from enums import Classification, Paycheck_Method

class Employee:
    '''develops a payroll program for a company'''
    def __init__(self, int:id, string:name, string:street_address, string:city,
                string:state, int:zipcode, classification=None, payment_Method,
                income, route, account):
        self.id = id
        self.name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification
        self.payment_Method = payment_Method
        self.salary = 0
        self.hourly = 0
        self.commission_rate = 0
        self.route = route
        self.account = account

        self.__set_income(income)

    def __set_income(self, money):
        if self.classification = Classification.SALARIED:
            self.salary = money[0]
        if self.classification = Classification.HOURLY:
            self.hourly = money[1]
        if self.classification = Classification.COMMISSIONED:
            self.commission_rate = money[2]

    def __get_income(self):
        if self.classification = Classification.SALARIED:
            return self.salary
        if self.classification = Classification.HOURLY:
            return self.hourly
        if self.classification = Classification.COMMISSIONED:
            return self.commission_rate

    def set_paycheck_method(self, method):
        self.payment_Method = method

    def get_pay(self):
        return [self.payment_Method, self.classification, self.__get_income()]

    def get_address(self):
        return (self.street_address + " " + self.city + ", " + self.state + " "
                + self.zipcode)

    def get_name(self):
        return self.name

    def save_employee(self):
        return (str(self.id) + ","
               +str(self.name) + ","
               +str(self.street_address) + ","
               +str(self.city) + ","
               +str(self.state) + ","
               +str(self.zip) + ","
               +str(self.classification) + ","
               +str(self.payment_Method) + ","
               +str(self.salary) + ","
               +str(self.hourly) + ","
               +str(self.commission_rate) + ","
               +str(self.route) + ","
               +str(self.account) + "\n")
