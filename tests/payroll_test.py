import unittest

from model.user import User
from controller.user_controller import UserController
from controller.payment_controller import PaymentController
from controller.employee_controller import EmployeeController
from service.file_helper import FileHelper

class TestPayroll(unittest.TestCase):

    def test_pay_str(self):
        original_pay = []
        FH = FileHelper.get_helper()
        with open(FH.get_adjusted_path("resources//payroll.txt")) as original:
            for line in original:
                original_pay.append(line)

        PCon = PaymentController.start_controller()
        PCon._EmpController.open_repo(FH.get_adjusted_path("/resources//employees.csv"))
        employee_list = list(PCon._EmpController.get_all_as_dict().values())

        test_pay = []
        for employee in employee_list:
            pay_str = PCon.get_pay_str(employee)
            test_pay.append(pay_str)

        self.assertListEqual(original_pay, test_pay)
