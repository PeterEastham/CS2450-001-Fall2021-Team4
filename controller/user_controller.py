"""
Make sure to only import this class after a successful login. The login_controller
is designed to pass in the current user after that, so you just need to use
the get_controller to get the reference. And make sure to log-out a user.
"""
from repo.userRepo import UserRepo
from model.user import User

from enums.permissions import Permission
from enums.controllers import Controller_Types as CT
from service.file_helper import FileHelper

class UserController:
    #Required for Singleton Behavior
    _UserInstance = None
    _CurrUser = None
    _UserRepo = None
    _FileHelper = None

    #This annotation allows us to call the function with calling __init__ first.
    @staticmethod
    def start_controller(Controller):
        if UserController._UserInstance == None:
            UserController(Controller)
        return UserController._UserInstance

    #This code mirrors start_controller(), but can only be called after it.
    #Increases readbility of code.
    @staticmethod
    def get_controller():
        if UserController._UserInstance != None:
            return UserController._UserInstance
        else:
            raise Exception("Start the Controller first")

    #This hits Itself and the Employee controller
    @staticmethod
    def stop_controller():
        if UserController._UserInstance != None:
            object = UserController._UserInstance
            object._EC.stop_controller()
            object._UserRepo.save_repo()

    #DO NOT CALL OUTSIDE OF start_controller!!
    def __init__(self, Controller):
        if UserController._UserInstance != None:
            raise Exception("This class is a Singleton!")
        else:
            UserController._UserInstance = self
            self._SuperController = Controller
            self._FileHelper = FileHelper.get_helper()
            empRepoPath = self._FileHelper.get_adjusted_path(".//resources//employees.csv")
            userRepoPath = self._FileHelper.get_adjusted_path(".//resources//users.csv")
            self._UserRepo = UserRepo(userRepoPath)
            self._EC = self._SuperController.get_a_controller(CT.EMPLOYEE_CONTROLLER)
            self._EC.open_repo(empRepoPath)
            #We'll store the User Repository here.
            #Users are Employees

    def login(self, user):
        if self._CurrUser != None:
            raise Exception("Cannot login a user until the current user logs out.")
        #Verify the user is a User Object
        if (type(user).__name__ != "User"):
            raise Exception("This is not a user object!")

        self._CurrUser = user

    def get_employee_dict(self):
        check = self.check_priviledge(Permission.CAN_VIEW_EMP.value, "View Employees")
        if check != None:
            return check

        return self._EC.get_all_as_dict()

    def can_create_user(self):
        check = self.check_priviledge(Permission.CAN_CREATE_USER.value, "Create New User")
        if check != None:
            return check

    #Adds to the UserRepo, we make sure to save the repo on every call.
    def create_new_user(self, username, password, permissions):
        self._UserRepo.add_one(User(username, password, permissions))
        self._UserRepo.save_repo()

    #Needs to pass in a User Object, we'll have to add in type testing at some point
    def adjust_permissions(self, user):
        check = self.check_priviledge(Permission.CAN_GIVE_PERM.value, "Adjust Permissions")
        if check != None:
            return check

        if user.employee_id == self._CurrUser.employee_id:
            self._CurrUser = user
            
        self._UserRepo.update_user(user)
        self._UserRepo.save_repo()

    #Used in Correlation with adjust_permissions()
    def get_user_by_username(self, username):
        check = self.check_priviledge(Permission.CAN_VIEW_EMP.value, "Get User")
        if check != None:
            return check

        return self._UserRepo.get_user_by_username(username)

    def get_user_by_emp_id(self, emp_id):
        return self._UserRepo.get_user_by_emp_id(emp_id)

    def get_employee_by_id(self, emp_id):
        check = self.check_priviledge(Permission.CAN_VIEW_EMP.value, "View Employee")
        if check != None:
            return check

        return self._EC.get_employee_by_id(emp_id)

    def make_payroll(self, emp_id_list):
        check = self.check_priviledge(Permission.MAKE_PAYROLL.value, "Make Payroll")
        if check != None:
            return check
        PCon = self._SuperController.get_a_controller(CT.PAYMENT_CONTROLLER)
        PCon.pay_emp_list(emp_id_list)
        self._SuperController.close_a_controller(CT.PAYMENT_CONTROLLER)


    #We've include self.check_user() since it would be called before this anyway.
    def check_priviledge(self, permission_value, permission_error):
        self.check_user()
        if not self._CurrUser.has_permission(permission_value):
            return(f"Current user does not have the {permission_error} permission")

    def check_user(self):
        if self._CurrUser == None:
            return("There is currently no user logged in!")

    def get_curr_user(self):
        return self._CurrUser

    #ANYTIME YOU NO LONGER KNOW THE USER
    #CALL THIS FUNCTION
    def logout(self):
        self._UserRepo.save_repo()
        self._CurrUser = None
        self._SuperController.close_a_controller(CT.EMPLOYEE_CONTROLLER)
