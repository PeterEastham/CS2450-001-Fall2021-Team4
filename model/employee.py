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
import re
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
        validator = EmployeeValidator.start_controller()
        self.valid = validator.validate(self)

    #Potentially could be removed if we decided to use file.writeLines()
    #But this maintains current format.
    def save_format(self):
        if not self.valid:
            raise Exception("Missing Save Params")

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


class EmployeeValidator():
    _EmpValInstance = None

    @staticmethod
    def start_controller():
        if EmployeeValidator._EmpValInstance == None:
            EmployeeValidator()
        return EmployeeValidator._EmpValInstance

    def __init__(self):
        if EmployeeValidator._EmpValInstance != None:
            raise Exception("This class is a singleton")
        else:
            EmployeeValidator._EmpValInstance = self

    def validate(self, employee):
        if not isinstance(employee, Employee):
            raise Exception("This is not an employee object!")
        else:
            status = self.validation_values(employee)
            return False if False in status.values() else True

    def validation_values(self, employee):
        status = self.base_dictionary()
        status |= self.validate_personal_info(employee, status)
        status |= self.validate_business_info(employee, status)
        status |= self.validate_address(employee, status)
        status |= self.validate_payment_info(employee, status)
        return status

    #Validates First/Last Name, and SSN.
    def validate_personal_info(self, employee, validation):
        if not isinstance(employee.first_name, str):
            validation["first_name"] = False
        if not isinstance(employee.last_name, str):
            validation["last_name"] = False

        validation["social_security"] = self.validate_with_regex(employee.social_security, "\d{3}-\d{2}-\d{3}")
        return validation


    def validate_business_info(self, employee, validation):
        if not isinstance(employee.title, str):
            validation["title"] = False
        if not isinstance(employee.department, str):
            validation["department"] = False

        validation["start_date"] = self.validate_with_regex(employee.start_date, "[0,1]\d/[0-3]\d/[1,2][0,9]\d\d")

        email_phone_result = (self.validate_with_regex(employee.office_email, ".+@.+\..{3}")
                             or self.validate_with_regex(employee.office_phone, "\(\d{3}\)\s\d{3}-\d{4}"))
        validation["office_email"],validation["office_phone"] = email_phone_result, email_phone_result
        return validation

    def validate_address(self, employee, validation):
        if not isinstance(employee.street_address, str):
            validation["street_address"] = False
        if not isinstance(employee.city, str):
            validation["city"] = False
        if not isinstance(employee.state, str):
            validation["state"] = False

        validation["zipcode"] = self.validate_zip(employee.zipcode)
        return validation

    def validate_payment_info(self, employee, validation):
        validation["classification"] = self.validate_int_range(employee.classification, [0,1,2])
        validation["payment_method"] = self.validate_int_range(employee.payment_Method, [0,1])

        if validation["classification"]:
            if employee.classification == Classification.SALARIED.value:
                validation["salary"] = self.validate_float(employee.salary)
            elif employee.classification == Classification.COMMISSIONED.value:
                validation["salary"] = self.validate_float(employee.salary)
                validation["rate"] = self.validate_float(employee.rate)
            else:
                validation["rate"] = self.validate_float(employee.rate)

        if validation["payment_method"]:
            if employee.payment_Method == Paycheck_Method.DIRECT_DEPOSIT.value:
                #Will be re-included once we know the format the professor plans on
                #validation["route"] = self.validate_routing_str(employee.route)
                validation["account"] = self.validate_account_number(employee.account)
        return validation

    def validate_float(self, salary):
        if not isinstance(salary, float):
            return False
        else:
            return True if salary > 0.0 else False

    def validate_int_range(self, num, num_range):
        if not isinstance(num, int):
            return False
        if not num in num_range:
            return False
        return True

    def validate_with_regex(self, input_str, format_str):
        if not isinstance(input_str, str) or not isinstance(format_str, str):
            return False
        tester = re.compile(format_str)
        result = tester.match(input_str)
        if isinstance(result, None.__class__):
            return False
        return True

    def validate_zip(self, zipcode):
        if not isinstance(zipcode, str):
            return False

        if len(zipcode) == 5:
            return self.validate_with_regex(zipcode, "\d{5}")

        if len(zipcode) == 9:
            return self.validate_with_regex(zipcode, "\d{5}-\d{4}")

        return False

    def validate_routing_str(self, routing_str):
        if not isinstance(routing_str, str):
            return False
        if len(routing_str) != 9:
            return False
        routing_num = [int(digit) for digit in routing_str]

        total = (3 * (routing_num[0] + routing_num[3] + routing_num[6])
                 + 7 * (routing_num[1] + routing_num[4] + routing_num[7])
                 + (routing_num[2] + routing_num[5] + routing_num[8]))

        return True if total % 10 == 0 else False

    def validate_account_number(self, account_str):
        if not isinstance(account_str, str):
            return False
        if len(account_str) < 6:
            return False
        if len(account_str) > 17:
            return False

        return True

    def base_dictionary(self):
        base = {
            "id" : True,
            "first_name" : True,
            "last_name" : True,
            "social_security" : True,
            "title" : True,
            "department" : True,
            "office_email" : True,
            "office_phone" : True,
            "start_date" : True,
            "street_address" : True,
            "city" : True,
            "state" : True,
            "zipcode" : True,
            "classification" : True,
            "payment_method" : True,
            "route" : True,
            "account" : True,
            "income" : True
        }
        return base
