

from model.user import User
from controller.user_controller import UserController

Admin = User("Admin", "YEP", "1:2:3:4")
UCon = UserController.start_controller()
UCon.login(Admin)

UCon.make_payroll()
