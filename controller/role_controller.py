"""
Handles different User interactions based on Roles.

"""
from enums.controllers import Controller_Types as CT

class RoleController():
    _RoleInstance = None

    @staticmethod
    def start_controller(Controller):
        if RoleController._RoleInstance == None:
            RoleController(Controller)
        return RoleController._RoleInstance

    @staticmethod
    def get_controller():
        if RoleController._RoleInstance != None:
            return RoleController._RoleInstance
        else:
            raise Exception("Start the Controller first")

    @staticmethod
    def close_controller():
        if RoleController._RoleInstance != None:
            object = RoleController._RoleInstance
            object._UserController = None
            RoleController._RoleInstance = None

    def __init__(self, Controller):
        if RoleController._RoleInstance != None:
            raise Exception("This class is a singleton")
        else:
            RoleController._RoleInstance = self
            self._SuperController = Controller
            self._UserController = self._SuperController.get_a_controller(CT.USER_CONTROLLER)
