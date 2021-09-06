"""
Accessing the "Employee" database. Which is really the CSV
"""

from model.employee import Employee
from service.version_handling import class_csv_headers
import csv

class EmployeeRepo():

    def __init__(self, repoPath=".//resources//employees.csv"):
        #We will pretend like we can't use CSV()
        self.repoPath = repoPath
        self.employees = []
        self.__load_repo()

    def __load_repo(self):
        with open(self.repoPath, 'r') as repo:
            reader = csv.DictReader(repo)
            for row in reader:
                self.add_one(row['ID'], row['Name'], row['Address'], row['City']
                , row['State'], row['Zip'], row['Classification'], row['PayMethod']
                , [row['Salary'], row['Hourly'], row['Commission']], row['Route']
                , row['Account'])

    def get_one_by_id(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                return employee

        return None

    def get_all_employees(self):
        return self.employees

    def add_one(self, id, name, street_address, city,
                state, zipcode, classification, payment_Method,
                income, route, account):
        self.employees.append(
                    Employee(id, name, street_address, city,
                    state, zipcode, classification, payment_Method,
                    income, route, account)
                    )

    def remove_one_by_id(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                self.employees.remove(employee)

    def save_repo(self):
        sorted_employees = sorted(self.employees, key=lambda Employee: Employee.id)
        with open((".//resources//test_file.csv"), 'w') as save_repo:
            save_repo.write(class_csv_headers(sorted_employees[0]))
            for employee in sorted_employees:
                save_repo.write(employee.save_format())


    def update_employee(self, employee):
        self.remove_one_by_id(employee.id)
        self.employees.append(employee)
