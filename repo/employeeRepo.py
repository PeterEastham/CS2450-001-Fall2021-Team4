"""
Accessing the "Employee" database. Which is really the CSV
Might need to create a mapper in /service if model changes are extreme.
"""

from repo.baseRepo import BaseCSVRepo
from service.version_handling import class_csv_headers
from model.employee import Employee

class EmployeeRepo(BaseCSVRepo):

    #We'll integrate old Employee Formats using this function.
    def make_object(self, dict_object):
        return Employee(dict_object['ID'], dict_object['Name'], dict_object['Address']
        , dict_object['City'], dict_object['State'], dict_object['Zip']
        , dict_object['Classification'], dict_object['PayMethod']
        , [ dict_object['Salary'], dict_object['Hourly'], dict_object['Commission'] ]
        , dict_object['Route'], dict_object['Account'])

    #So nice.
    def save_objects_list(self):
        sorted_employees = sorted(self.objects, key=lambda Employee: Employee.id)
        headers = class_csv_headers(sorted_employees[0])
        save_list = []
        save_list.append(headers)
        for employee in sorted_employees:
            save_list.append(employee.save_format())

        return save_list
