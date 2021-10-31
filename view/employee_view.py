import tkinter as tk
from tkinter import ttk
from enums.controllers import Controller_Types as CT
from service.enum_converter import convert_classification, convert_payment_method

class EmployeeViewPage(tk.Tk):

    """View Page"""
    def __init__(self, Controller, employee):
        super().__init__()

        self.geometry("600x400")
        self.title("Employee View")
        self.resizable(0, 0)
        self._SuperController = Controller
        self.__employee = employee
        self.create_employee_str_vars(employee)
        self.create_title_labels()
        self.create_info_labels()
        self.create_timecard_box()
        self.create_button_str_var()
        self.create_buttom_buttons()
        self.base_view()

    def swap_to_edit(self):
        print("Swap to Edit")
        #self.create_edit_labels_and_boxes(self.__employee)

    def create_employee_str_vars(self, employee):
       """Creates labels and boxes for the base view."""
       PCon = self._SuperController.get_a_controller(CT.PAYMENT_CONTROLLER)

       self.id = tk.StringVar(self, value=employee.id)
       self.first_name = tk.StringVar(self, value=employee.first_name)
       self.last_name = tk.StringVar(self, value=employee.last_name)
       self.social_security = tk.StringVar(self, value=employee.social_security)
       self.state = tk.StringVar(self, value=employee.state)
       self.city = tk.StringVar(self, value=employee.city)
       self.street_address = tk.StringVar(self, value=employee.street_address)
       self.zipcode = tk.StringVar(self, value=employee.zipcode)

       self.title = tk.StringVar(self, value=employee.title)
       self.department = tk.StringVar(self, value=employee.department)
       self.office_email = tk.StringVar(self, value=employee.office_email)
       self.office_phone = tk.StringVar(self, value=employee.office_phone)
       self.start_date = tk.StringVar(self, value=employee.start_date)

       self.salary = tk.StringVar(self, value=employee.salary)
       self.rate = tk.StringVar(self, value=employee.rate)
       self.route = tk.StringVar(self, value=employee.route)
       self.account = tk.StringVar(self, value=employee.account)
       self.next_payroll = tk.StringVar(self, value="{:.2f}".format(PCon.get_pay(employee.id)))
       self.classification = tk.StringVar(self, value=convert_classification(employee.classification))
       self.payment_method = tk.StringVar(self, value=convert_payment_method(employee.payment_Method))


    def create_title_labels(self):
        self.id_title_lb = ttk.Label(self, text="Employee Id")
        self.first_name_title_lb = ttk.Label(self, text="First name")
        self.last_name_title_lb = ttk.Label(self, text="Last name")
        self.social_security_title_lb = ttk.Label(self, text="Social Security")
        self.state_title_lb = ttk.Label(self, text="State")
        self.city_title_lb = ttk.Label(self, text="City")
        self.street_address_title_lb = ttk.Label(self, text="Address")
        self.zipcode_title_lb = ttk.Label(self, text="Zipcode")

        self.title_title_lb = ttk.Label(self, text="Title")
        self.department_title_lb = ttk.Label(self, text="Department")
        self.office_email_title_lb = ttk.Label(self, text="Office Email")
        self.office_phone_title_lb = ttk.Label(self, text="Office Phone")
        self.start_date_title_lb = ttk.Label(self, text="Start Date")

        self.salary_title_lb = ttk.Label(self, text="Salary")
        self.rate_title_lb = ttk.Label(self, text="Commission")
        self.route_title_lb = ttk.Label(self, text="Route")
        self.account_title_lb = ttk.Label(self, text="Account")
        self.classification_title_lb = ttk.Label(self, text="Classification")
        self.payment_method_title_lb = ttk.Label(self, text="Payment Method")
        self.next_payroll_title_lb = ttk.Label(self, text="Next Payroll Amount")

    def create_button_str_var(self):
        self.left_button_str = tk.StringVar(self, value="Return to Search")
        self.right_button_str = tk.StringVar(self, value="Edit")

    def create_buttom_buttons(self):
        self.left_button = ttk.Button(self, textvariable=self.left_button_str)
        self.right_button = ttk.Button(self, textvariable=self.right_button_str, command=self.swap_to_edit)

    def create_timecard_box(self):
        self.box_lb = ttk.Label(self, text="Receipts/Timecards")
        self.receipts_timecards_scrollbox = tk.Scrollbar(self)
        self.the_list_box = tk.Listbox(self)

    def create_info_labels(self):
        self.id_lb = ttk.Label(self, textvariable=self.id)
        self.first_name_lb = ttk.Label(self, textvariable=self.first_name)
        self.last_name_lb = ttk.Label(self, textvariable=self.last_name)
        self.social_security_lb = ttk.Label(self, textvariable=self.social_security)
        self.state_lb = ttk.Label(self, textvariable=self.state)
        self.city_lb = ttk.Label(self, textvariable=self.city)
        self.street_address_lb = ttk.Label(self, textvariable=self.street_address)
        self.zipcode_lb = ttk.Label(self, textvariable=self.zipcode)

        self.title_lb = ttk.Label(self, textvariable=self.title)
        self.department_lb = ttk.Label(self, textvariable=self.department)
        self.office_email_lb = ttk.Label(self, textvariable=self.office_email)
        self.office_phone_lb = ttk.Label(self, textvariable=self.office_phone)
        self.start_date_lb = ttk.Label(self, textvariable=self.start_date)

        self.salary_lb = ttk.Label(self, textvariable=self.salary)
        self.rate_lb = ttk.Label(self, textvariable=self.rate)
        self.route_lb = ttk.Label(self, textvariable=self.route)
        self.account_lb = ttk.Label(self, textvariable=self.account)
        self.next_payroll_lb = ttk.Label(self, textvariable=self.next_payroll)
        self.classification_lb = ttk.Label(self, textvariable=self.classification)
        self.payment_method_lb = ttk.Label(self, textvariable=self.payment_method)


    def base_view(self):
        # PERSONAL INFO #
        self.id_title_lb.grid(column=0, row=0)
        self.id_lb.grid(column=1, row=0)

        self.first_name_title_lb.grid(column=0, row=1)
        self.first_name_lb.grid(column=0, row=2)

        self.last_name_title_lb.grid(column=1, row=1)
        self.last_name_lb.grid(column=1, row=2)

        self.social_security_title_lb.grid(column=2, row=0)
        self.social_security_lb.grid(column=2, row=1)

        self.state_title_lb.grid(column=0, row=3)
        self.state_lb.grid(column=0, row=4)

        self.city_title_lb.grid(column=1, row=3)
        self.city_lb.grid(column=1, row=4)

        self.street_address_title_lb.grid(column=0, row=5)
        self.street_address_lb.grid(column=0, row=6)

        self.zipcode_title_lb.grid(column=2, row=3)
        self.zipcode_lb.grid(column=2, row=4)

        # COMPANY INFO #
        self.title_title_lb.grid(column=0,row=7)
        self.title_lb.grid(column=1, row=7)

        self.department_title_lb.grid(column=0, row=8)
        self.department_lb.grid(column=1, row=8)

        self.office_email_title_lb.grid(column=0, row=9)
        self.office_email_lb.grid(column=1, row=9)

        self.office_phone_title_lb.grid(column=0, row=10)
        self.office_phone_lb.grid(column=1, row=10)

        self.start_date_title_lb.grid(column=0, row=11)
        self.start_date_lb.grid(column=1, row=11)

        # PAYMENT INFORMATION #
        self.classification_title_lb.grid(column=0, row=12)
        self.classification_lb.grid(column=1, row=12)

        self.payment_method_title_lb.grid(column=0, row=13)
        self.payment_method_lb.grid(column=1, row=13)

        self.salary_title_lb.grid(column=0, row=14)
        self.salary_lb.grid(column=1, row=14)

        self.rate_title_lb.grid(column=0, row=15)
        self.rate_lb.grid(column=1, row=15)

        self.next_payroll_title_lb.grid(column=0, row=16)
        self.next_payroll_lb.grid(column=1, row=16)

        self.route_title_lb.grid(column=2, row=13)
        self.route_lb.grid(column=2, row=14)

        self.account_title_lb.grid(column=3, row=13)
        self.account_lb.grid(column=3, row=14)


        # BOTTOM BUTTONS #
        self.left_button.grid(column=0, row=17)
        self.right_button.grid(column=1, row=17)

        # scrollbar and listbox for the receipts and timecards

        self.box_lb.grid(column=4, row=0)
        self.the_list_box.grid(column=4, rowspan=8, row=1)
        self.receipts_timecards_scrollbox.grid(column=4, rowspan=8, row=1)
