"""
Accessing the "Employee" database. Which is really the CSV
Might need to create a mapper in /service if model changes are extreme.
"""

from repo.baseRepo import BaseCSVRepo
from service.version_handling import class_csv_headers
from service.employee_factory import EmployeeFactory
from model.employee import Employee

class EmployeeRepo(BaseCSVRepo):

    #We'll integrate old Employee Formats using this function.
    def make_object(self, dict_object):
        header = self.make_header_from_keys(dict_object)
        return EmployeeFactory.create_employee(header, dict_object)

    #So nice.
    def save_objects_list(self):
        sorted_employees = sorted(self.objects, key=lambda Employee: Employee.id)
        headers = class_csv_headers(sorted_employees[0])
        save_list = []
        save_list.append(headers)
        for employee in sorted_employees:
            save_list.append(employee.save_format())

        return save_list
