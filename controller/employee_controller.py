"""
Handles the Employee Model
New Employees, Deleting Employees, Etc

This Class should only accept Employee Information.
We only calculate/set Employee information through this.
Retrieving Payment Information is allowed as that is a sub-component of Employees.

Payment Amount/Str is not calculated in here as that *uses* employees, not is part of them.
"""
#TODO - Make EmployeeController a wrapper for receipt/timecard controller.
#Before inputing to receipt/timecard repos, verify they belong to a valid employee.
#For reporting purposes, give employees an "active" property, and don't delete them directly.
from repo.employeeRepo import EmployeeRepo
class EmployeeController():
    _EmpRepo = None #This might be converted to a list to allow for Employee Database Imports.
                    #Since a requirement of the shareholder is DB exporting.
    _EmpInstance = None

    @staticmethod
    def start_controller():
        if EmployeeController._EmpInstance == None:
            EmployeeController()
        return EmployeeController._EmpInstance

    #We might put the initial repo string in here.
    def __init__(self):
        if EmployeeController._EmpInstance != None:
            raise Exception("This class is a singleton")
        else:
            EmployeeController._EmpInstance = self

    #get_controller()? check_controller()? <- Mirror start_controller, just for readability.

    def open_repo(self, repoPath):
        if self._EmpRepo != None:
            raise Exception("Only one Employee Database may be open!")
        else:
            self._EmpRepo = EmployeeRepo(repoPath)

    #Create an export_repo(str) to meet Shareholder Requirements.
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
            self._EmpRepo.add_one(Employee(id, name, street_address, city, state,
                                  zipcode, classification, payment_Method,
                                  income, route, account))

    #We'll stick to emp_id since Employee.name might not be unique.
    def get_employee_by_id(self, emp_id):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            return self._EmpRepo.get_one_by_id(emp_id)

    #Dictionary format is {"Name" : ID}
    def get_all_as_dict(self):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            employeeSource = self._EmpRepo.get_all()
            employee_dict = dict()
            for employee in employeeSource:
                employee_dict[employee.name] = employee.id
            return employee_dict

    #UserController should wrap this.
    def remove_employee(self, emp_id):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            self._EmpRepo.remove_one_by_id(emp_id)

    #Validate input?
    def update_address(self, employee, new_street_address, new_city, new_state,
                       new_zipcode):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            employee.street_address = new_street_address
            employee.city = new_city
            employee.state = new_state
            employee.zipcode = new_zipcode
            self._EmpRepo.update_object(employee)
            return employee
            #Rework the flow to be something like.
            #GUI.on_save() -> EC.get_employee_by_id(emp_id)
            #Then have this return true/false?

    #TODO, implement XD
    def update_classification(self):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            pass

    #Needs validation to check for bank information if method == Direct Deposit
    def update_payment_method(self, employee, new_payment_method):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            employee.payment_Method = new_payment_method
            self._EmpRepo.update_object(employee)
            return employee
            #See note on update_address()


    #Noted in the employee.py file, but it might be worth caching the old value.
    def update_payment_rate(self, employee, new_payment_rate):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            employee.set_income(new_payment_method)
            self._EmpRepo.update_object(employee)
            return employee

    #def predict_pay(new_classification)? Expected Values should ~= Old Values.
    #Examples of Salary -> Hourly. Salary / 2000 = Hourly
    #Reverse holds true as well.


    def get_pay(self, emp_id):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
           return self._EmpRepo.get_one_by_id(emp_id).get_pay()


    #Call this method during make_employee()
    def _verify_employee(self):
        pass

    #We'll put these here, _verify_employee should use them, but the update methods
    #Should use this as well.
    def _verify_address(self):
        pass

    #Figure out how Routing/Banking Numbers are composed.
    def _verify_banking(self):
        pass

    #Can we stick this into an annotation?
    def __no_emp_repo(self):
        raise Exception("You need to open a Repository before using this!")
