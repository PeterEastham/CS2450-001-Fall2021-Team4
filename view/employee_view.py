import tkinter as tk
from tkinter import ttk
from enums.controllers import Controller_Types as CT

class EmployeeViewPage(tk.Tk):

    """View Page"""
    def __init__(self, Controller, employee):
        super().__init__()

        self.geometry("600x400")
        self.title("Employee View")
        self.resizable(0, 0)
        self._SuperController = Controller
        # if employee != None:
        #     self.view_employee(employee)
        # else:
        #     self.base_view()
        self.base_view()

    def view_employee(self, employee):
        # first and last name text boxes & labels

        first_name_lb = ttk.Label(self, text="Name")
        first_name_lb.grid(column=0, row=1, sticky="W")

        first_name_box = ttk.Label(self, width=12, text=employee.get_full_name())
        first_name_box.grid(column=0, row=2)

        # city and classification boxes & labels

        city_label = ttk.Label(self, text="Address")
        city_label.grid(column=0, row=3, sticky = "W")

        city_box = ttk.Label(self, width=25, text=employee.get_address())
        city_box.grid(column=0, row=4)

        classification_label = ttk.Label(text="Classification")
        classification_label.grid(column=0, row=5)

        classification_box = ttk.Label(self, width=20, text=employee.classification)
        classification_box.grid(column=0, row=3)

        # payment information text boxes and labels

        salary_label = ttk.Label(text="Salary")
        salary_label.grid(column=0, row=7)

        # salary_box = ttk.Label(self, width=20, text=employee.salary)
        # salary_box.grid(column=0, row=8, padx=10)

        rate_label = ttk.Label(text="Commission")
        rate_label.grid(column=2, row=7)
        print(self.grid_size())

        # rate_box = ttk.Label(self, width=20, text=employee.rate)
        # rate_box.grid(column=2, row=8)

        next_payroll_label = ttk.Label(text="Next Payroll Amount")
        next_payroll_label.grid(column=1, row=9)

        # next_pay = self._SuperController.get_a_controller(CT.EMPLOYEE_CONTROLLER).get_pay(employee.id)
        # next_payroll_box = ttk.Label(self, width=25, text=next_pay)
        # next_payroll_box.grid(column=1, row=10, pady=5)

        # close and edit buttons

        close_button = ttk.Button(self, text="Close")
        close_button.grid(column=0, row=12)

        edit_button = ttk.Button(self, text="Edit")
        edit_button.grid(column=1, row=12)

        box_label = ttk.Label(text="Receipts/Timecards")
        box_label.grid(column=6, row=10)

        the_list_box = tk.Listbox(self)
        the_list_box.grid(column=4, rowspan=2, row=3, sticky="E")

        receipts_timecards_scrollbox = tk.Scrollbar(self)
        receipts_timecards_scrollbox.grid(column=5, rowspan=3, row=1, sticky="NS")

    def base_view(self):

        # first and last name text boxes & labels

        first_name_lb = ttk.Label(self, text="First name")
        first_name_lb.grid(column=0, row=1)

        self.first_name = tk.StringVar(value="")
        first_name_box = ttk.Entry(self, width=12, textvariable=self.first_name)
        first_name_box.grid(column=0, row=2)

        last_name_lb = ttk.Label(self, text="Last name")
        last_name_lb.grid(column=2, row=1)

        self.last_name = tk.StringVar(value="")
        last_name_box = ttk.Entry(self, width=12, textvariable=self.last_name)
        last_name_box.grid(column=2, row=2)

        # city and classification boxes & labels

        city_label = ttk.Label(self, text="City")
        city_label.grid(column=1, row=3)

        self.city = tk.StringVar(value="")
        city_box = ttk.Entry(self, width=25, textvariable=self.city)
        city_box.grid(column=1, row=4)

        classification_label = ttk.Label(text="Classification")
        classification_label.grid(column=1, row=5)

        self.classification = tk.StringVar(value="")
        classification_box = ttk.Entry(self, width=20, textvariable=self.classification)
        classification_box.grid(column=1, row=6)

        # payment information text boxes and labels

        salary_label = ttk.Label(text="Salary")
        salary_label.grid(column=0, row=7)

        self.salary = tk.StringVar(value="")
        salary_box = ttk.Entry(self, width=20, textvariable=self.classification)
        salary_box.grid(column=0, row=8, padx=10)

        rate_label = ttk.Label(text="Commission")
        rate_label.grid(column=2, row=7)

        self.rate = tk.StringVar(value="")
        rate_box = ttk.Entry(self, width=20, textvariable=self.rate)
        rate_box.grid(column=2, row=8)

        next_payroll_label = ttk.Label(text="Next Payroll Amount")
        next_payroll_label.grid(column=1, row=9)

        self.next_payroll = tk.StringVar(value="")
        next_payroll_box = ttk.Entry(self, width=25, textvariable=self.next_payroll)
        next_payroll_box.grid(column=1, row=10, pady=5)

        # close and edit buttons

        close_button = ttk.Button(self, text="Close")
        close_button.grid(column=0, row=12)

        edit_button = ttk.Button(self, text="Edit")
        edit_button.grid(column=1, row=12)


        # scrollbar and listbox for the receipts and timecards

        box_label = ttk.Label(text="Receipts/Timecards")
        box_label.grid(column=6, row=10, columnspan=2)

        self.the_list_box = tk.Listbox(self)
        self.the_list_box.grid(column=6, rowspan=2, row=11, sticky="E")

        receipts_timecards_scrollbox = tk.Scrollbar(self)
        receipts_timecards_scrollbox.grid(column=7, rowspan=2, row=11, sticky="NS")
