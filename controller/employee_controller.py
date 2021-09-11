"""
Handles the Employee Model
New Employees, Deleting Employees, Etc

This Class should only accept Employee Information.
We only calculate/set Employee information through this.
Retrieving Timecards is allowed as that is a sub-component of Employees.

Payment is not calculated in here as that *uses* employees, not is part of them.
"""
from repo.employeeRepo import EmployeeRepo
class EmployeeController():
    _EmpRepo = None
    _EmpInstance = None

    @staticmethod
    def start_controller():
        if EmployeeController._EmpInstance == None:
            EmployeeController()
        return EmployeeController._EmpInstance

    def __init__(self):
        if EmployeeController._EmpInstance != None:
            raise Exception("This class is a singleton")
        else:
            EmployeeController._EmpInstance = self

    def open_repo(self, repoPath):
        if self._EmpRepo != None:
            raise Exception("Only one Employee Database may be open!")
        else:
            self._EmpRepo = EmployeeRepo(repoPath)

    def close_repo(self):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            self._EmpRepo.save_repo()
            self._EmpRepo = None

    #Note, Income = [Salary, Hourly, Commission]
    def make_new_employee(self, id, name, street_address, city,
                state, zipcode, classification, payment_Method,
                income, route, account):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            self._EmpRepo.add_one(id, name, street_address, city, state,
                                  zipcode, classification, payment_Method,
                                  income, route, account)

    def get_employee_by_id(self, emp_id):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            return self._EmpRepo.get_one_by_id(emp_id)

    def remove_employee(self, emp_id):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            self._EmpRepo.remove_one_by_id(emp_id)

    def update_address(self, employee, new_street_address, new_city, new_state,
                       new_zipcode):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            employee.street_address = new_street_address
            employee.city = new_city
            employee.state = new_state
            employee.zipcode = new_zipcode
            self._EmpRepo.update_employee(employee)
            return employee

    def update_classification(self):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            pass

    def update_payment_method(self, employee, new_payment_method):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            employee.payment_Method = new_payment_method
            self._EmpRepo.update_employee(employee)
            return employee


    def update_payment_rate(self, employee, new_payment_rate):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            employee.set_income(new_payment_method)
            self._EmpRepo.update_employee(employee)
            return employee

    def get_pay(self, emp_id):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
           return self._EmpRepo.get_one_by_id(emp_id).get_pay()


    #Call this method during make_employee()
    def _verify_employee(self):
        pass

    def __no_emp_repo(self):
        raise Exception("You need to open a Repository before using this!")
