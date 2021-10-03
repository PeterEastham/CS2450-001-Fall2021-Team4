"""
Handles Payment.

Primarly Focused on a Functional Approach to increase Testability.
Can Accept Employee/Timecard/Receipt objects/references.

An Employee's Information IS NOT CALCULATED IN HERE. Please insert any
employee logic into the Employee Controller, it is more readable.

payment_controller should be wrapped by user_controller, use this for test,
but not really for anything else.
"""

from model.employee import Employee
from model.receipt import Receipt
from controller.employee_controller import EmployeeController
from controller.receipt_controller import ReceiptController
from controller.timecard_controller import TimeCardController
from enums.classification import Classification
from enums.paycheck_method import Paycheck_Method
from service.file_helper import FileHelper

class PaymentController():
    _EmpController = None
    _TimeCardController = None
    _RecController = None
    _PaymentInstance = None
    _FileHelper = None
    #Might be useful to input a "Valid Employee" check in the EC, then allow function
    #Execution.

    @staticmethod
    def start_controller():
        if PaymentController._PaymentInstance == None:
            PaymentController()
        return PaymentController._PaymentInstance

    def __init__(self):
        if PaymentController._PaymentInstance != None:
            raise Exception("This class is a singleton")
        else:
            PaymentController._PaymentInstance = self
            self._FileHelper = FileHelper.get_helper()
            self.update_emp_controller()
            self.update_receipt_controller()
            self.update_timecard_controller()

    #These three functions are to verify the other controllers have started.
    def update_emp_controller(self):
        self._EmpController = EmployeeController.start_controller()

    def update_receipt_controller(self):
        self._RecController = ReceiptController.start_controller()
        self._RecController.open_repo("")

    def update_timecard_controller(self):
        self._TimeCardController = TimeCardController.start_controller()
        self._TimeCardController.open_repo("")


    #emp_list is an int list of employee IDs.
    def pay_emp_list(self, emp_list):
        payroll_path = self._FileHelper.get_adjusted_path("payrolltest.txt")
        with open(payroll_path, 'w') as payroll:
            pay = []
            for emp_id in emp_list:
                pay_str = self.get_pay_str(emp_id)
                pay.append(pay_str)

            payroll.writelines(pay)


    #Reference the Enum module for exact values.
    def get_pay_str(self, emp_id):
        pay = self._EmpController.get_pay(emp_id)
        payment_method = pay[0] #Note that if get_pay() changes, this will break.
        income = self.get_pay(emp_id) #self.get_pay is a better wrapper for EC.get_pay()

        #These if statement construct the payroll string for us.
        #We don't want the logic in this function.
        if payment_method == Paycheck_Method.DIRECT_DEPOSIT.value:
            return self._direct_payment(emp_id).format(income)
        if payment_method == Paycheck_Method.MAIL.value:
            return self._mailing_payment(emp_id).format(income)


    #This method uses an employee_id so that we can calculate the income
    #of an employee without needing to get a full string. This really returns
    #a double.
    def get_pay(self, emp_id):
        pay = self._EmpController.get_pay(emp_id)
        classification = pay[1]
        income = 0
        if classification == Classification.COMMISSIONED.value:
            return self._is_commissioned(emp_id, pay[2])

        if classification == Classification.SALARIED.value:
            return self._is_salaried(pay[2])

        if classification == Classification.HOURLY.value:
            return self._is_hourly(emp_id, pay[2])

    #Handlers for different Payment.
    #In theory we could use subclasses of employee, but this is the main differences,
    #As such it's easier to treat them as the same, and filter by a property.
    def _is_commissioned(self, emp_id, income):
        return (float(income[0]) + #Income = Salary + Receipts * Commission Rate.
               (self._RecController.get_receipt_total(emp_id) * float(income[1])))

    def _is_salaried(self, salary): #Might be broken.
        return (float(salary) / 24) #We store the Annual, so we need to calculate the bi-weekly.
            #In theory we might offer different payment times, so 24 might become a parameter.

    def _is_hourly(self, emp_id, rate):
        return (self._TimeCardController.get_total_hours(emp_id) * float(rate))
            #Income = Hours * Pay_Rate


    def _mailing_payment(self, emp_id):
        employee = self._EmpController.get_employee_by_id(emp_id)
        return "Mailing {} to {} at {}\n".format("{:.2f}", #.2f means a floating point rounded to 2 digits.
                                        employee.get_full_name(), employee.get_address())

    def _direct_payment(self, emp_id):
        employee = self._EmpController.get_employee_by_id(emp_id) #See Above.
        return "Transferred {} for {} to {} at {}\n".format("{:.2f}", employee.get_full_name(),
                                                   employee.account, employee.route)
