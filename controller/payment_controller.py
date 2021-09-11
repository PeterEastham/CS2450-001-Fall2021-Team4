"""
Handles Payment.

Primarly Focused on a Functional Approach to increase Testability.
Can Accept Employee/Timecard/Receipt objects/references.

An Employee's Information IS NOT CALCULATED IN HERE. Please insert any
employee logic into the Employee Controller, it is more readable.
"""

from model.employee import Employee
from model.receipt import Receipt
from controller.employee_controller import EmployeeController
from controller.receipt_controller import ReceiptController
from controller.timecard_controller import TimeCardController
from enums.classification import Classification
from enums.paycheck_method import Paycheck_Method

class PaymentController():
    _EmpController = None
    _TimeCardController = None
    _RecController = None
    _PaymentInstance = None

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
            self.update_emp_controller()
            self.update_receipt_controller()
            self.update_timecard_controller()


    def update_emp_controller(self):
        self._EmpController = EmployeeController.start_controller()

    def update_receipt_controller(self):
        self._RecController = ReceiptController.start_controller()

    def update_timecard_controller(self):
        self._TimeCardController = TimeCardController.start_controller()

    def get_pay_str(self, emp_id):
        pay = self._EmpController.get_pay(emp_id)
        method = pay[0]
        income = self.get_pay(emp_id)
        if method == Paycheck_Method.DIRECT_DEPOSIT.value:
            return self._direct_payment(emp_id).format(income)
        if method == Paycheck_Method.MAIL.value:
            return self._mailing_payment(emp_id).format(income)
        print(f"There was no method: {method}")

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
        print(f"There was no classification: {classification}")

    def _is_commissioned(self, emp_id, income):
        return (float(income[0]) +
               (self._RecController.get_receipt_total(emp_id) * float(income[1])))

    def _is_salaried(self, salary):
        return (float(salary) / 24)

    def _is_hourly(self, emp_id, rate):
        return (self._TimeCardController.get_total_hours(emp_id) * float(rate))

    def _mailing_payment(self, emp_id):
        employee = self._EmpController.get_employee_by_id(emp_id)
        return "Mailing {} to {} at {}".format("{:.2f}",
                                        employee.name, employee.get_address())

    def _direct_payment(self, emp_id):
        employee = self._EmpController.get_employee_by_id(emp_id)
        return "Transferred {} for {} to {} at {}".format("{:.2f}", employee.name,
                                                   employee.account, employee.route)
