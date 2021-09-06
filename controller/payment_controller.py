"""
Handles Payment.

Primarly Focused on a Functional Approach to increase Testability.
Can Accept Employee/Timecard/Receipt objects/references.

An Employee's Information IS NOT CALCULATED IN HERE. Please insert any
employee logic into the Employee Controller, it is more readable.
"""

from model.employee import Employee
from model.receipt import Receipt
from employee_controller import *
from receipt_controller import *
from enums.classification import Classification
from enums.paycheck_method import Paycheck_Method


def get_pay(emp):
    pay = employee_controller.get_pay(emp)
    method = employee_controller.get_method(())
    classification = employee_controller.get_classification()
    if classification == Classification.COMMISSIONED:
        _is_commissioned(pay)

    if classification == Classification.SALARIED:
        _is_salaried(pay)

    if classification == Classification.HOURLY:
        _is_hourly(pay)

def _is_commissioned(receipts):
    pass

def _is_salaried(salary):
    pass

def _is_hourly(hourly_rate):
    pass
