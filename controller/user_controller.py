"""
Make sure to only import this class after a successful login. The login_controller
is designed to pass in the current user after that, so you just need to use
the get_controller to get the reference. And make sure to log-out a user.
"""
from repo.userRepo import UserRepo
from model.user import User
from enums.permissions import Permission
from controller.employee_controller import EmployeeController
from controller.payment_controller import PaymentController

class UserController:
    #Required for Singleton Behavior
    _UserInstance = None
    _CurrUser = None
    _UserRepo = None

    #This annotation allows us to call the function with calling __init__ first.
    @staticmethod
    def start_controller():
        if UserController._UserInstance == None:
            UserController()
        return UserController._UserInstance

    #This code mirrors start_controller(), but can only be called after it.
    #Increases readbility of code.
    @staticmethod
    def get_controller():
        if UserController._UserInstance != None:
            return UserController._UserInstance
        else:
            raise Exception("Start the Controller first")

    #DO NOT CALL OUTSIDE OF start_controller!!
    def __init__(self):
        if UserController._UserInstance != None:
            raise Exception("This class is a Singleton!")
        else:
            UserController._UserInstance = self
            self._UserRepo = UserRepo()
            self._EC = EmployeeController.start_controller()
            self._EC.open_repo(".//resources//employees.csv")
            #We'll store the User Repository here.
            #User != Employee!!!!

    def login(self, user):
        if self._CurrUser != None:
            raise Exception("Cannot login a user until the current user logs out.")
        #Verify the user is a User Object
        if (type(user).__name__ != "User"):
            raise Exception("This is not a user object!")

        self._CurrUser = user

    def get_employee_list(self):
        self.check_priviledge(Permission.CAN_VIEW_EMP.value, "View Employees")

        return self._EC.get_all_as_dict()


    #Adds to the UserRepo, we make sure to save the repo on every call.
    def create_new_user(self, username, password, permissions):
        self.check_privliedge(Permission.CAN_CREATE_USER.value, "Create new User")

        self._UserRepo.add_one(User(username, password, permissions))
        self._UserRepo.save_repo()

    #Needs to pass in a User Object, we'll have to add in type testing at some point
    def adjust_permissions(self, user):
        self.check_priviledge(Permission.CAN_GIVE_PERM.value, "Adjust Permissions")

        self._UserRepo.update_user(user)
        self._UserRepo.save_repo()

    #Used in Correlation with adjust_permissions()
    def get_user_by_username(self, username):
        self.check_priviledge(Permission.CAN_VIEW_EMP.value, "Get User")

        return self._UserRepo.get_user_by_username(username)

    def make_payroll(self):
        self.check_priviledge(Permission.MAKE_PAYROLL.value, "Make Payroll")
        Emp_list = list(self._EC.get_all_as_dict().values())
        PCon = PaymentController.start_controller()
        PCon.pay_emp_list(Emp_list)



    #We've include self.check_user() since it would be called before this anyway.
    def check_priviledge(self, permission_value, permission_error):
        self.check_user()
        if not self._CurrUser.has_permission(permission_value):
            raise Exception(f"Current user does not have the {permission_error} permission")

    def check_user(self):
        if self._CurrUser == None:
            raise Exception("There is currently no user logged in!")



    #ANYTIME YOU NO LONGER KNOW THE USER
    #CALL THIS FUNCTION
    def logout(self):
        self._UserRepo.save_repo()
        self._UserRepo = None
        self._CurrUser = None
        UserController._UserInstance = None
