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

    @staticmethod
    def get_controller():
        if EmployeeController._EmpInstance != None:
            return EmployeeController._EmpInstance
        else:
            raise Exception("Start the Controller first")

    @staticmethod
    def stop_controller():
        if EmployeeController._EmpInstance != None:
            EmployeeController._EmpInstance.close_repo()
            EmployeeController._EmpInstance = None
            EmployeeController._EmpRepo = None

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

    #Created an to meet Shareholder Requirements.
    def close_repo(self):
        if self._EmpRepo != None:
            self._EmpRepo.save_repo()
            self._EmpRepo = None

    #Note, Income = [Salary, Hourly, Commission]
    #NEED TO REDO THIS
    def make_new_employee(self, dict_object):
        pass

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
                employee_dict[employee.get_reversed_name()] = employee.id
            return employee_dict

    #UserController should wrap this.
    def remove_employee(self, emp_id):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            self._EmpRepo.remove_one_by_id(emp_id)

    def update_employee(self, changed_employee):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
            self._EmpRepo.update_object(changed_employee)


    def get_pay(self, emp_id):
        if self._EmpRepo == None:
            self.__no_emp_repo()
        else:
           return self._EmpRepo.get_one_by_id(emp_id).get_pay()


    #Can we stick this into an annotation?
    def __no_emp_repo(self):
        raise Exception("You need to open a Repository before using this!")
