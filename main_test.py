import sys
import unittest

from tests.payroll_test import TestPayroll
from tests.service_test import ServiceModuleTest
from service.file_helper import FileHelper
from controller.controller_controller import Controller
from view.login_page import main as main
from pprint import pprint

"""
Entry Point for the testing service, we'll be able to use this
in order to force the testing to use a different source repository.
"""

if __name__ == "__main__":
    FileHelper.start_helper(".//" + sys.argv[0][:-12] + "/tests/")
    Con = Controller.start_controller()
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPayroll))
    suite.addTest(unittest.makeSuite(ServiceModuleTest))
    result = runner.run(suite)
    print(f"Tests Run {result.testsRun}")
    print(f"Error Total {len(result.errors)}")
    print(f"Failure Total {len(result.failures)}")
    # print(result.buffer)
    # main(Con)
    # DO NOT RUN THE TESTS IF YOU PLAN TO GO INTO THE GUI.
    # They currently break each other.
