"""
We can nickname this "HR".

I'm moving Employee Creation into this since there is different ways we can
handle the "versioning" of different employees. This is just a method that
reduces the amount of logic for creating an employee, inside that employee.
"""
from model.employee import Employee
from .version_handling import *

class EmployeeFactory():

    @staticmethod
    def create_employee(repo_header, dict_row):
        version = header_to_version[repo_header]

        if version == "emp_1.0":
            return EmployeeFactory.version_one(dict_row)

    @staticmethod
    def version_one(dict_row):
        base = EmployeeFactory.base_dictionary()

        base['id'] = dict_row["ID"]

        names = dict_row['Name'].split(" ", 1)
        base['first_name'] = names[0]
        base['last_name'] = names[1]

        base["archived"] = False
        base["imported"] = True
        base["street_address"] = dict_row["Address"]
        base["city"] = dict_row["City"]
        base["state"] = dict_row["State"]
        base["zipcode"] = dict_row["Zip"]
        base["classification"] = dict_row["Classification"]
        base["payment_method"] = dict_row["PayMethod"]
        base["income"] = [dict_row["Salary"], dict_row["Hourly"], dict_row["Commission"]]
        base["route"] = dict_row["Route"]
        base["account"] = dict_row["Account"]

        return Employee(base)


    @staticmethod
    def base_dictionary():
        base = {
            "id" : None,
            "first_name" : None,
            "last_name" : None,
            "archived" : False,
            "social_security" : None,
            "title" : None,
            "department" : None,
            "office_email" : None,
            "office_phone" : None,
            "start_date" : None,
            "imported" : False,
            "street_address" : None,
            "city" : None,
            "state" : None,
            "zipcode" : None,
            "classification" : None,
            "payment_method" : None,
            "route" : None,
            "account" : None,
            "income" : None
        }
        return base
