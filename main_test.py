import sys
import unittest

from tests.payroll_test import TestPayroll
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
    result = runner.run(unittest.makeSuite(TestPayroll))
    print(f"Tests Run {result.testsRun}")
    print(f"Error Total {len(result.errors)}")
    print(f"Failure Total {len(result.failures)}")
