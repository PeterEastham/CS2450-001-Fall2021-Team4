"""
Accessing the "Employee" database. Which is really the CSV
Might need to create a mapper in /service if model changes are extreme.
"""

from model.employee import Employee
from service.version_handling import class_csv_headers
from service.file_helper import FileHelper as FH
import csv

class EmployeeRepo():
    #Note, this repoPath CAN change, but should be verified before passing in.
    #We'll assume the file holds valid Employee Data.
    def __init__(self, repoPath=".//resources//employees.csv"):
        file_aid = FH.get_helper()
        self.repoPath = file_aid.get_cwd_path(repoPath)
        self.employees = []
        self.__load_repo()

    #In case the data is in a bad format, we need to catch an exception.
    #Verify with the Shareholder that we can use the csv module, this was
    #banned in CS1410.
    def __load_repo(self):
        with open(self.repoPath, 'r') as repo:
            reader = csv.DictReader(repo)
            for row in reader:
                self.add_one(row['ID'], row['Name'], row['Address'], row['City']
                , row['State'], row['Zip'], row['Classification'], row['PayMethod']
                , [row['Salary'], row['Hourly'], row['Commission']], row['Route']
                , row['Account']) #Might have to change it with the mapper.

    def get_one_by_id(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                return employee
        return None #Raise an exception instead?

    def get_all_employees(self):
        return self.employees
        #So simple, so beautiful.

    #We'll assume that if the EC calls this, the data is verified.
    #Might want a check for a unique ID? See if we assign the ID, or if that
    #is passed in. Check ID collisions first though.
    def add_one(self, id, name, street_address, city,
                state, zipcode, classification, payment_Method,
                income, route, account):
        self.employees.append(
                    Employee(id, name, street_address, city,
                    state, zipcode, classification, payment_Method,
                    income, route, account)
                    )

    #ONLY REMOVE BY ID, we can't assume that names are unique.
    def remove_one_by_id(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                self.employees.remove(employee)

    #Sort by key is amazing.
    #See about filtering other id-based repos this way.
    #We might make repoPath a parameter so export_repo() can wrap this.
    def save_repo(self):
        sorted_employees = sorted(self.employees, key=lambda Employee: Employee.id)
        with open((self.repoPath), 'w') as save_repo:
            save_repo.write(class_csv_headers(sorted_employees[0]))
            for employee in sorted_employees:
                save_repo.write(employee.save_format())

    #Assume valid data from the EC.
    #Noted in Add One, but id collisions might be needed to be handled.
    def update_employee(self, employee):
        self.remove_one_by_id(employee.id)
        self.employees.append(employee)
