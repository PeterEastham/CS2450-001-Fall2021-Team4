import tkinter as tk
from tkinter import ttk


class LoginPage(tk.Tk):
    """Class for the login page"""
    def __init__(self):
        super().__init__()

        self.geometry("300x100")
        self.title('Login')
        self.resizable(0, 0)

        # grid config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):
        """Create widgets for username, password and login button"""

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,  show="*")
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


def main():
    app = LoginPage()
    app.mainloop()


if __name__ == "__main__":
    main()


