"""
Page to Create/Edit Users
"""
import tkinter as tk
from tkinter import ttk
from enums.permissions import Permission, display_name
from enums.controllers import Controller_Types as CT

class UserPanel(tk.Tk):

    def __init__(self, SuperController, SearchWindow, employee_id):
        super().__init__()
        print(f"Employee Id { employee_id }")
        self._SuperController = SuperController
        self.__SearchWindow = SearchWindow
        SearchWindow.toggle_window_disable()
        self.protocol('WM_DELETE_WINDOW', self.close_instance)

        self.geometry("450x250")
        self.title("User Panel")
        self.resizable(0, 0)
        self.UC = self._SuperController.get_a_controller(CT.USER_CONTROLLER)
        self._CurrUser = self.UC.get_curr_user()
        self.give_permissions = []
        self.has_permissions = []

        if employee_id == None:
            employee_id = self._CurrUser.employee_id
        self.set_user(employee_id)
        self.reset()


    def close_instance(self):
        self.__SearchWindow.toggle_window_disable()
        self.destroy()

    def set_user(self, employee_id):
        self.User = self.UC.get_user_by_emp_id(employee_id)
        if isinstance(self.User, type(None)):
            self.Employee = self.UC.get_employee_by_id(employee_id)
            self.create_user()
        else:
            self.view_user()


    def create_user(self):
        self.create_widgets()
        self.giveable_permissions()
        self.username.set(self.Employee.get_combined_name())

    def giveable_permissions(self):
        self.temp = [f"Can {display_name[perm]}" for perm in self._CurrUser.permissions]
        self.give_permissions = [value for value in self.temp
                                        if value not in self.has_permissions]

    def view_user(self):
        self.create_widgets()
        self.owned_permissions()
        if self.User.employee_id != self._CurrUser.employee_id:
            self.giveable_permissions()
        self.username.set(self.User.username)

    def owned_permissions(self):
        self.has_permissions = [f"Can {display_name[perm]}" for perm in self.User.permissions]

    def move_items_lr(self):

        curr = list(self.left_list_box.curselection())
        if len(curr) == 0:
            return
        list.sort(curr, reverse=True)
        self.left_list_box.selection_clear(0, tk.END)
        for index in curr:
            self.right_list_box.insert(tk.END, self.left_list_box.get(index))
            self.left_list_box.delete(index)

    def move_items_rl(self):

        curr = list(self.right_list_box.curselection())
        if len(curr) == 0:
            return
        list.sort(curr, reverse=True)
        self.right_list_box.selection_clear(0, tk.END)
        for index in curr:
            self.left_list_box.insert(tk.END, self.right_list_box.get(index))
            self.right_list_box.delete(index)

    def reset(self):
        self.clear_side(self.left_list_box)
        self.clear_side(self.right_list_box)
        self.fill_side(self.left_list_box)
        self.fill_side(self.right_list_box)

    #We'll use in combination with "Select All"
    def fill_side(self, side):
        if side == self.left_list_box:
            for index, perm in enumerate(self.give_permissions):
                side.insert(index, perm)
        else:
            for index, perm in enumerate(self.has_permissions):
                side.insert(index, perm)

    def clear_side(self, side):
        side.delete(0, tk.END)

    def select_all(self):
        self.clear_side(self.right_list_box)
        self.clear_side(self.left_list_box)
        index = 0
        for ind, value in enumerate(self.has_permissions):
            index = ind
            self.right_list_box.insert(index, value)
        for value in self.give_permissions:
            index += 1
            self.right_list_box.insert(index, value)

    def attempt_save(self):
        pass


    def create_widgets(self):

        self.left_list_lb = ttk.Label(self, text="Giveabled Permissions")
        self.left_list_lb.grid(column=0, row=1)
        self.left_list_box = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.left_list_box.grid(column=0, row=2)

        self.right_list_lb = ttk.Label(self, text="Owned Permissions")
        self.right_list_lb.grid(column=2, row=1)
        self.right_list_box = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.right_list_box.grid(column=2, row=2, sticky="NS")

        # add button
        self.add_button = ttk.Button(self, text="Add->", command=self.move_items_lr)
        self.add_button.grid(column=1, row=1, sticky="N")

        # add all button
        self.add_all_button = ttk.Button(self, text="Add All", command=self.select_all)
        self.add_all_button.grid(column=1, row=2, sticky="N", pady=30)

        self.reset_button = ttk.Button(self, text="Reset", command=self.reset)
        self.reset_button.grid(column=1, row=2)

        # remove Button
        self.remove_button = ttk.Button(self, text="<-Remove", command=self.move_items_rl)
        self.remove_button.grid(column=1, row=2, sticky="S")


        self.username_lb = ttk.Label(self, text="Username")
        self.password_lb = ttk.Label(self, text="Password")
        self.username_lb.grid(column=3, row=1, sticky="N")
        self.password_lb.grid(column=3, row=3, sticky="N")

        self.username = tk.StringVar(self, value="")
        self.username_label = ttk.Label(self, textvariable=self.username)
        self.username_label.grid(column=3, row=2, sticky="N")

        self.password_label = ttk.Label(self, text="********")
        self.password_label.grid(column=3, row=4, sticky="N")

        self.save_button  = ttk.Button(self, text="Save", command=self.attempt_save)
        self.save_button.grid(column=0, row=4)

        self.close_button = ttk.Button(self, text="Close", command=self.close_instance)
        self.close_button.grid(column=2, row=4)
