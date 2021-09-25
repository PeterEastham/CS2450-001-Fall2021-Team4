"""
Can search for specific employees.
Flows into an Employee Viewer
Log-Out button call user_controller, and then goes back to the Login-Page /w the
login_controller
"""
from controller.user_controller import UserController


#You can use CTRL + L to uncomment these, in case you don't know.

#
# def __init__(self):
#     self.UC = UserController.get_controller()
#

#Store this dictionary somewhere so you can reference it.
#The keys are the emplyoee names, and they map to their ID's.
# def employee_names(self):
#     employees = UserController.get_employee_list()
#     return list(employees.keys())
#

# def load_information(self):
#   employee = UserController.get_employee_by_id(employees[selected_username])
#   load_new_frame(employee)?
#
