"""
Used to convert an Enum value into an actual String
"""
from enums.classification import Classification
from enums.paycheck_method import Paycheck_Method

def convert_classification(enum_value):
    if enum_value == Classification.COMMISSIONED or enum_value == Classification.COMMISSIONED.value:
        return "Commissioned"
    if enum_value == Classification.SALARIED or enum_value == Classification.SALARIED.value:
        return "Salaried"
    if enum_value == Classification.HOURLY or enum_value == Classification.HOURLY.value:
        return "Hourly"


def convert_payment_method(enum_value):
    if enum_value == Paycheck_Method.DIRECT_DEPOSIT or enum_value == Paycheck_Method.DIRECT_DEPOSIT.value:
        return "Direct Deposit"
    if enum_value == Paycheck_Method.MAIL or enum_value == Paycheck_Method.MAIL.value:
        return "Mail"


def reverse_classification_convert(str_value):
    if str_value == "Commission":
        return Classification.COMMISSIONED
    if str_value == "Salary":
        return Classification.SALARIED
    if str_value == "Hourly":
        return Classification.HOURLY

def reverse_payment_method_convert(str_value):
    if str_value == "Mail":
        return Paycheck_Method.MAIL
    if str_value == "Direct Deposit":
        return Paycheck_Method.DIRECT_DEPOSIT
