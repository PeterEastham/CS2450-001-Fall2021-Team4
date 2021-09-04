"""
Handles the Employee Model
New Employees, Deleting Employees, Etc

This Class should only accept Employee Information.
We only calculate/set Employee information through this.
Retrieving Timecards is allowed as that is a sub-component of Employees.

Payment is not calculated in here as that *uses* employees, not is part of them.
"""
from repo import EmployeeRepo
_EmpRepo = None

def start_controller(string:repoPath=".//resources//employees.csv"):
    _EmpRepo = EmployeeRepo(repoPath)

def make_employee():
    pass

def remove_employee(emp_id):
    _EmpRepo.remove_one_by_id(emp_id)

def update_address(emp_id, ):
    pass

def update_classification():
    pass

def update_payment_method():
    pass

def update_payment_rate():
    pass

#should only be called by the payment_controller
def get_pay():
    pass

#Call this method during make_employee()
def _verify_employee():
    pass

def get_payment_method():
    pass

def get_classication():
    pass
