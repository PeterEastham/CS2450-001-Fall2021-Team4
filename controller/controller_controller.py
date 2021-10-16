"""
Needed a way to standardize the controller behavior.
Right now it's hard for a controller to know if another controller has been started.
There is also a bit of an issue handling the "Repositories", example issue that could
come up.

I want to view an employee, EmployeeController provides me the information regarding
the TimeCard for that employee on the view screen. I want to calculate his pay,
I ask the payment controller, which either has to A, restart the timecard_controller (slow)
or B, tries to open the timecard repository and causes an "Already Open" Exception.

This Controller will act as a messager for all the controllers, handling the current
state of the controller, and making it so we can standardize behavior.

It gets started in main.py, and never closes until the program finishes.

"""
from .employee_controller import EmployeeController
from .login_controller import LoginController
from .payment_controller import PaymentController
from .receipt_controller import ReceiptController
from .timecard_controller import TimeCardController
from .user_controller import UserController
from .role_controller import RoleController

from enums.controllers import Controller_Types as CT



class Controller():
    _ControllerInstance = None

    @staticmethod
    def start_controller():
        if Controller._ControllerInstance == None:
            Controller()
        return Controller._ControllerInstance

    @staticmethod
    def get_controller():
        if Controller._ControllerInstance != None:
            return Controller._ControllerInstance
        else:
            raise Exception("Start the Controller first")

    def __init__(self):
        if Controller._ControllerInstance != None:
            raise Exception("This class is a singleton")
        else:
            #Order is INCREDIBLY IMPORTANT HERE
            Controller._ControllerInstance = self
            self._RecCon = [ReceiptController.start_controller(), True]
            self._TimCon = [TimeCardController.start_controller(), True]
            self._LogCon = [LoginController.start_controller(self), True]
            self._EmpCon = [EmployeeController.start_controller(), True]
            self._PayCon = [PaymentController.start_controller(self), True]
            self._UserCon = [UserController.start_controller(self), True]
            self._RoleCon = [RoleController.start_controller(self), True]

    def get_a_controller(self, request):
        controller_response = None
        if request == CT.EMPLOYEE_CONTROLLER:
            controller_response = self._handle_status(request, True)
        elif request == CT.PAYMENT_CONTROLLER:
            controller_response = self._handle_status(request, True)
        elif request == CT.RECEIPT_CONTROLLER:
            controller_response = self._handle_status(request, True)
        elif request == CT.TIMECARD_CONTROLLER:
            controller_response = self._handle_status(request, True)
        elif request == CT.USER_CONTROLLER:
            controller_response = self._handle_status(request, True)
        elif request == CT.LOGIN_CONTROLLER:
            controller_response = self._handle_status(request, True)
        elif request == CT.ROLE_CONTROLLER:
            controller_response = self._handle_status(request, True)
        else:
            raise Exception("Invalid Request!")
        return controller_response

    def close_a_controller(self, request):
        controller_response = None
        if request == CT.EMPLOYEE_CONTROLLER:
            controller_response = self._handle_status(request, False)
        elif request == CT.PAYMENT_CONTROLLER:
            controller_response = self._handle_status(request, False)
        elif request == CT.RECEIPT_CONTROLLER:
            controller_response = self._handle_status(request, False)
        elif request == CT.TIMECARD_CONTROLLER:
            controller_response = self._handle_status(request, False)
        elif request == CT.USER_CONTROLLER:
            controller_response = self._handle_status(request, False)
        elif request == CT.LOGIN_CONTROLLER:
            controller_response = self._handle_status(request, False)
        elif request == CT.ROLE_CONTROLLER:
            controller_response = self._handle_status(request, False)
        else:
            raise Exception("Invalid Request!")

    def close_all_controllers(self):
        self._UserCon[0].stop_controller()
        self._PayCon[0].close_controller()

    # requested_status == True, self._Controller[1] == True - Return Controller
    # requested_status == True, self._Controller[1] == False - Return Controller
    # requested_status == False, self._Controller[1] == True - Set [1] to false
    # requested_status == False, self._Controller[1] == False - Raise Exception
    def _handle_status(self, request, requested_status):
        requested_controller = None
        if request == CT.EMPLOYEE_CONTROLLER:
            requested_controller = self._EmpCon
        elif request == CT.PAYMENT_CONTROLLER:
            requested_controller = self._PayCon
        elif request == CT.RECEIPT_CONTROLLER:
            requested_controller = self._RecCon
        elif request == CT.TIMECARD_CONTROLLER:
            requested_controller = self._TimCon
        elif request == CT.USER_CONTROLLER:
            requested_controller = self._UserCon
        elif request == CT.LOGIN_CONTROLLER:
            requested_controller = self._LogCon
        elif request == CT.ROLE_CONTROLLER:
            requested_controller = self._RoleCon

        if requested_status and requested_controller[1]:
            return requested_controller[0]
        if requested_status and not requested_controller[1]:
            return requested_controller[0]
        if not requested_status and requested_controller[1]:
            requested_controller[1] = False

        return None
