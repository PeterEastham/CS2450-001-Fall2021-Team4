import tkinter as tk
from tkinter import ttk
from functools import wraps

from enums.controllers import Controller_Types as CT
from view.employee_view import EmployeeViewPage
from view.notification import Notification
from view.user_control_panel import UserPanel
"""
This Class is the landing page after a successful login.

We pass in the Constructor to the Login-Page as well, we'll likely
want to convert that into a list for when we have multiple possible pages.

We use the UserController from this point to handle data, but we'll also pass
in the SuperController so that we can give the LoginPage the LoginController on
Logout.
"""

class EmployeeSearchPage(tk.Tk):
    """Search Page """
    def __init__(self, Controller):
        super().__init__()

        self.geometry("550x250")
        self.title('Employee Search')
        self.resizable(0, 0)
        self.disable = False
        self._SuperController = Controller
        self.UC = self._SuperController.get_a_controller(CT.USER_CONTROLLER)
        # grid config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close_application)

    def pass_in_login_construc(self, login_constr):
        self._login_constr = login_constr

    def toggle_window_disable(self):
        self.disable = not self.disable

    def move_items_lr(self):
        if self.disable:
            return

        curr = list(self.left_list_box.curselection())
        if len(curr) == 0:
            return
        list.sort(curr, reverse=True)
        self.left_list_box.selection_clear(0, tk.END)
        for index in curr:
            self.right_list_box.insert(tk.END, self.left_list_box.get(index))
            self.left_list_box.delete(index)

    def move_items_rl(self):
        if self.disable:
            return

        curr = list(self.right_list_box.curselection())
        if len(curr) == 0:
            return
        list.sort(curr, reverse=True)
        self.right_list_box.selection_clear(0, tk.END)
        for index in curr:
            self.left_list_box.insert(tk.END, self.right_list_box.get(index))
            self.right_list_box.delete(index)

    #We'll use in combination with "Select All"
    def fill_side(self, side):
        if self.disable:
            return

        for index, emp in enumerate(self.emp_dict):
            side.insert(index, emp)

    def clear_side(self, side):
        if self.disable:
            return
        else:
            side.delete(0, tk.END)

    def select_all(self):
        self.clear_side(self.left_list_box)
        self.clear_side(self.right_list_box)
        self.fill_side(self.right_list_box)

    def reset(self):
        if self.disable:
            return

        self.clear_side(self.left_list_box)
        self.clear_side(self.right_list_box)
        self.fill_side(self.left_list_box)

    def make_user(self):
        if self.disable:
            return

        selected_index = self.right_list_box.curselection()
        if len(selected_index) == 0:
            selected_index = self.left_list_box.curselection()
            if len(selected_index) != 0:
                selected_emp_id = self.left_list_box.get(selected_index[0])
                selected_emp_id = self.emp_dict[selected_emp_id]
            else:
                selected_emp_id = self.UC.get_curr_user().employee_id
        else:
            selected_emp_id = self.right_list_box.get(selected_index[0])
            selected_emp_id = self.emp_dict[selected_emp_id]

        user_panel = UserPanel(self._SuperController, self, selected_emp_id)
        user_panel.mainloop()


    def view_employee(self):
        if self.disable:
            return

        selected_index = self.right_list_box.curselection()
        selected_emp_id = None
        if len(selected_index) == 0:
            selected_index = self.left_list_box.curselection()
        else:
            selected_emp_id = self.right_list_box.get(selected_index[0])

        if len(selected_index) == 0:
            return

        if selected_emp_id == None:
            selected_emp_id = self.left_list_box.get(selected_index[0])

        selected_emp_id = self.emp_dict[selected_emp_id]
        target_emp = self.UC.get_employee_by_id(selected_emp_id)
        view_window = EmployeeViewPage(self._SuperController, self, target_emp)
        view_window.mainloop()


    def do_payroll(self):
        if self.disable:
            return

        names = self.right_list_box.get(0,tk.END)
        id_list = [self.emp_dict.get(name) for name in names]
        self.UC.make_payroll(id_list)

    def close_application(self):
        if self.disable:
            return

        self._SuperController.close_all_controllers()
        self.destroy()

    def do_logout(self):
        if self.disable:
            return

        self.UC.logout()
        self.destroy()
        LoginPage = self._login_constr(self._SuperController)
        LoginPage.mainloop()

    def add_employee(self):
        if self.disable:
            return None
        check = self.UC.can_create_user()
        if check != None:
            Notif = Notification(check, self)
            Notif.mainloop()
            return None

        view_window = EmployeeViewPage(self._SuperController, self, None)
        view_window.mainloop()

    def get_emp_dict(self):
        self.emp_dict = self.UC.get_employee_dict()
        if isinstance(self.emp_dict, str):
            Notif = Notification(self.emp_dict, self)
            Notif.mainloop()
        else:
            self.reset()

    def create_widgets(self):
        """Create widgets for Employee Search Page"""
        # search label
        search_label = ttk.Label(self, text="Search")
        search_label.grid(column=0, row=0)

        # search box
        self.search_box = tk.StringVar(value="NOT IMPLEMENTED")
        username_entry = ttk.Entry(self, textvariable=self.search_box)
        username_entry.grid(column=0, row=1)

        # left side list box
        self.left_list_box = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.left_list_box.grid(column=0, row=2)

        # right list box
        self.right_list_box = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.right_list_box.grid(column=2, row=2, sticky="NS")

        self.get_emp_dict()

        # scroll bar for left side list box
        left_scrollbar = tk.Scrollbar(self)
        left_scrollbar.grid(column=0, row=2, sticky="NSE")
        left_scrollbar.config(command=self.left_list_box.yview)

        # add button
        add_button = ttk.Button(self, text="Add->", command=self.move_items_lr)
        add_button.grid(column=1, row=1, sticky="N")

        # add all button
        add_all_button = ttk.Button(self, text="Add All", command=self.select_all)
        add_all_button.grid(column=1, row=2, sticky="N", pady=30)

        reset_button = ttk.Button(self, text="Reset", command=self.reset)
        reset_button.grid(column=1, row=2)

        # remove Button
        remove_button = ttk.Button(self, text="<-Remove", command=self.move_items_rl)
        remove_button.grid(column=1, row=2, sticky="S")


        # scroll bar for right side list box
        right_scrollbar = tk.Scrollbar(self)
        right_scrollbar.grid(column=2, row=2, stick="NSE")
        right_scrollbar.config(command=self.right_list_box.yview)

        # view employee button
        view_button = ttk.Button(self, text="View Employee", command=self.view_employee)
        view_button.grid(column=2, row=1)

        add_emp_button = ttk.Button(self, text = "Make Employee", command=self.add_employee)
        add_emp_button.grid(column=3, row=1, sticky="N", padx=40)

        # pay button
        pay_button = ttk.Button(self, text="Pay\nEmployees", command=self.do_payroll)
        pay_button.grid(column=3, row=2, sticky="S", padx=30)

        # Make User
        make_user = ttk.Button(self, text="Edit/Add User", command=self.make_user)
        make_user.grid(column=3, row=2, sticky="N", pady=30)

        # logout button
        logout_button = ttk.Button(self, text="Logout", command=self.do_logout)
        logout_button.grid(column=3, row=2, padx=30)
