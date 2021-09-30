import sys
import unittest

from tests.payroll_test import TestPayroll
from tests.service_test import ServiceModuleTest
from service.file_helper import FileHelper
from view.login_page import main as main
from pprint import pprint

"""
Entry Point for the testing service, we'll be able to use this
in order to force the testing to use a different source repository.
"""

if __name__ == "__main__":
    FileHelper.start_helper(".//" + sys.argv[0][:-12] + "/tests/")
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTests([unittest.makeSuite(TestPayroll), unittest.makeSuite(ServiceModuleTest)])
    result = runner.run(suite)
    print(f"Tests Run {result.testsRun}")
    print(f"Error Total {len(result.errors)}")
    print(f"Failure Total {len(result.failures)}")
    pprint(result.buffer)
