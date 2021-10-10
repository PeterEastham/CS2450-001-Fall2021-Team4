import tkinter as tk
from tkinter import ttk
from enums.controllers import Controller_Types as CT
from view import search_page as search


class LoginPage(tk.Tk):

    @staticmethod
    def bypass(Controller):
        return LoginPage(Controller.get_a_controller(CT.LOGIN_CONTROLLER), Controller)

    """Class for the login page"""
    def __init__(self, LoginCon, Controller):
        super().__init__()
        self.LC = LoginCon
        self._SuperController = Controller

        self.geometry("300x100")
        self.title('Login')
        self.resizable(0, 0)

        # grid config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def validate_wrapper(self, *args):
        self.validate_test()

    def validate_test(self):
        if self.LC.validate(self._username_input.get(), self._password_input.get()):
            Controller = self._SuperController
            Controller.close_a_controller(CT.LOGIN_CONTROLLER)
            del self._username_input
            del self._password_input
            self.destroy()
            new_window = search.EmployeeSearchPage(Controller)
            new_window.pass_in_login_construc(LoginPage.bypass)
            new_window.mainloop()

    def create_widgets(self):
        """Create widgets for username, password and login button"""

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)


        self._username_input = tk.StringVar()
        username_entry = ttk.Entry(self, textvariable=self._username_input)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self._password_input = tk.StringVar()
        password_entry = ttk.Entry(self,  show="*", textvariable=self._password_input)
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login", command=self.validate_test)
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.bind_all('<Key-Return>', self.validate_wrapper)


def main(Controller):
    LoginCon = Controller.get_a_controller(CT.LOGIN_CONTROLLER)
    app = LoginPage(LoginCon, Controller)
    app.mainloop()


if __name__ == "__main__":
    main()
