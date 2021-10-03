import sys

from service.file_helper import FileHelper
from view.login_page import main as main

# from tests import payroll_test
"""
We'll use this as an entry point.

#TODO.
Initialize all the objects we'll need.
Validators
Log-in Controller is currently handled by the
Login Page, but we might look into changing that.
"""

if __name__ == "__main__":
    FileHelper.start_helper(sys.argv[0][:-7])
    main()
