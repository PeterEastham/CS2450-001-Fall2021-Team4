"""
We'll view this as a functional approach to Property validation.

We'll use the Singleton pattern for simplicity's sake. Also because
it's better then dealing with multiple different objects.
"""
from model.Employee import Employee
from enums.classification import Classification
from enums.paycheck_method import Paycheck_Method
import re

class EmployeeValidator():
    _EmpValInstance = None

    @startmethod
    def start_controller(self):
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

    #Validates First/Last Name, and SSN.
    def validate_personal_info(self, employee, validation):
        if not isinstance(employee.first_name, str):
            validation["first_name"] = False
        if not isinstance(employee_last_name, str):
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
            if employee.payment_Method == PayCheck_Method.DIRECT_DEPOSIT.value:
                validation["route"] = self.validate_routing_str(employee.route)
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

        total = (3(routing_num[0] + routing_num[3] + routing_num[6])
                 + 7(routing_num[1] + routing_num[4] + routing_num[7])
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
