"""
Used as a lightweight method of login the user in.
As it stands, it will likely get merged with a
"user_controller" in the near future.
"""


from repo.userRepo import UserRepo
from model.user import User

class LoginController():
    _UserRepo = None
    _UserInstance = None

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
            LoginController._UserRepo = UserRepo()

    def validate(self, username, password):
        return self._UserRepo.validLogin(username, password)

    def getUser(self, username):
        return self._UserRepo.get_user_by_username(username)

    def stop_controller(self):
        self._UserInstance = None
        self._UserRepo = None
