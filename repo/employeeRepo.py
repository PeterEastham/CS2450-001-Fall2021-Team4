"""
Accessing the "Employee" database. Which is really the CSV
"""

from model import Employee

#TODO: Parse the File
    #SPIKE possible options for DB version handling
#TODO: Singultine Approach, Refactor all databases.
class EmployeeRepo():

    def __init__(self, repoPath=".//resources//employees.csv"):
        #We will pretend like we can't use CSV()
        self.repoPath = repoPath
        self.employees = []
        pass

    def get_one_by_id(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                return employee

        return None

    def get_all_employees(self):
        return self.employees

    def add_one(self, int:id, string:name, string:street_address, string:city,
                string:state, int:zipcode, classification=None, payment_Method,
                income, route, account):
        self.employees.append(
                    _create_employee(id, name, street_address, city,
                    state, zipcode, classification, payment_Method,
                    income, route, account)
                    )

    def _create_employee(int:id, string:name, string:street_address, string:city,
                string:state, int:zipcode, classification=None, payment_Method,
                income, route, account):

        emp = Employee(id, name, street_address, city, state, zipcode,
                       classification, payment_Method, income, route, account)

        return emp

    def remove_one_by_id(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                self.employees.remove(employee)

    def save_repo(self):
        #file logic, save each employee
        sorted_employees = sorted(self.employess, key=lambda Employee: Employee.id)
        pass

    def update_employee(self, employee):
        self.remove_one_by_id(employee.id)
        self.employees.append(employee)
