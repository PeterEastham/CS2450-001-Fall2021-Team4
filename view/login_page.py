import tkinter as tk
from tkinter import ttk
from controller.login_controller import LoginController
from view import search_page as search


class LoginPage(tk.Tk):
    """Class for the login page"""
    def __init__(self, LoginCon):
        super().__init__()
        self.LC = LoginCon

        self.geometry("300x100")
        self.title('Login')
        self.resizable(0, 0)

        # grid config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def validate_test(self):
        if self.LC.validate(self.username_input.get(),self.password_input.get()):
            self.destroy()
            new_window = search.EmployeeSearchPage()
            new_window.mainloop()

    def create_widgets(self):
        """Create widgets for username, password and login button"""

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)


        self.username_input = tk.StringVar(value="")
        username_entry = ttk.Entry(self, textvariable=self.username_input)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.password_input = tk.StringVar(value="")
        password_entry = ttk.Entry(self,  show="*", textvariable=self.password_input)
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login", command=self.validate_test)
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


def main():
    LoginCon = LoginController.start_controller()
    app = LoginPage(LoginCon)
    app.mainloop()


if __name__ == "__main__":
    main()
