import unittest

from model.user import User
from controller.controller_controller import Controller
from enums.controllers import Controller_Types as CT
from service.file_helper import FileHelper

class TestPayroll(unittest.TestCase):

    def test_pay_str(self):
        original_pay = []
        FH = FileHelper.get_helper()
        with open(FH.get_adjusted_path("resources//payroll.txt")) as original:
            for line in original:
                original_pay.append(line)

        Con = Controller.get_controller()
        PCon = Con.get_a_controller(CT.PAYMENT_CONTROLLER)
        employee_list = list(PCon._EmpController.get_all_as_dict().values())

        test_pay = []
        for employee in employee_list:
            pay_str = PCon.get_pay_str(employee)
            test_pay.append(pay_str)

        PCon._EmpController.close_repo()
        for pay_line in test_pay:
            self.assertIn(pay_line, original_pay)
        Con.close_a_controller(CT.EMPLOYEE_CONTROLLER)
        Con.close_a_controller(CT.PAYMENT_CONTROLLER)
