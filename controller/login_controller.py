"""
Used as a lightweight method of login the user in.
As it stands, it will likely get merged with a
"user_controller" in the near future.
"""


from repo.userRepo import UserRepo
from model.user import User
from controller.user_controller import UserController
from service.file_helper import FileHelper

#Changing a Password is a user_controller function!!
class LoginController():
    _UserRepo = None
    _UserInstance = None
    _FileHelper = None

    @staticmethod
    def start_controller():
        if LoginController._UserInstance == None:
            LoginController()
        return LoginController._UserInstance

    def __init__(self):
        if LoginController._UserInstance != None:
            raise Exception("This class is a singleton")
        else:
            LoginController._UserInstance = self
            self._FileHelper = FileHelper.get_helper()
            repoPath = self._FileHelper.get_adjusted_path(".//resources//users.csv")
            self._UserRepo = UserRepo(repoPath)

    #We'll pass in the user directly to the UserController, that way the
    #GUI never gets the User object directly, it's easier to test this way.
    def validate(self, username, password):
        if self._UserRepo.validLogin(username, password):
            UC = UserController.start_controller()
            currUser = self._UserRepo.get_user_by_username(username)
            UC.login(currUser)
            return True
        else:
            return False


    def stop_controller(self):
        self._UserInstance = None
        self._UserRepo = None
