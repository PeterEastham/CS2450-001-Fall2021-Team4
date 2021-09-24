"""
This class can be seen as a wrapper for the entire controller framework
this is because we'll be routing all of the GUI functionality after
login through this controller, which will allow us to handle permissions.
"""
from repo.userRepo import UserRepo
from model.user import User
from enums.permissions import Permission

class UserController:
    _UserInstance = None
    _CurrUser = None
    _UserRepo = None

    @staticmethod
    def start_controller():
        if UserController._UserInstance == None:
            UserController()
        return UserController._UserInstance

    @staticmethod
    def get_controller():
        if UserController._UserInstance != None:
            return UserController._UserInstance
        else:
            raise Exception("Please provide the current User first")

    def __init__(self):
        if UserController._UserInstance != None:
            raise Exception("This class is a Singleton!")
        else:
            UserController._UserInstance = self
            UserController._UserRepo = UserRepo()

    def login(self, user):
        if self._CurrUser != None:
            raise Exception("Cannot login a user until the current user logs out.")
        else:
            self._CurrUser = user

    def create_new_user(self, username, password, permissions):
        self.check_user()
        if not self._CurrUser.has_permission(Permission.CAN_CREATE_USER.value):
            self.insufficent_priviledge("Create new User")
        else:
            self._UserRepo.add_one(User(username, password, permissions))
            self._UserRepo.save_repo()

    def adjust_permissions(self, user):
        self.check_user()
        if not self._CurrUser.has_permission(Permission.CAN_GIVE_PERM.value):
            self.insufficent_priviledge("Adjust Permission")
        else:
            self._UserRepo.update_user(user)
            self._UserRepo.save_repo()

    def get_user_by_username(self, username):
        self.check_user()
        if not self._CurrUser.has_permission(Permission.CAN_VIEW_EMP.value):
            self.insufficent_priviledge("Get User")
        else:
            return self._UserRepo.get_user_by_username(username)

    def insufficent_priviledge(self, permission):
        raise Exception(f"Current user does not have the {permission} permission")

    def logout(self):
        self._UserRepo.save_repo()
        self._UserRepo = None
        self._CurrUser = None
        UserController._UserInstance = None

    def check_user(self):
        if self._CurrUser == None:
            raise Exception("There is currently no user logged in!")
