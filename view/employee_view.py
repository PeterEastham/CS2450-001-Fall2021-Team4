import tkinter as tk
from tkinter import ttk
from enums.controllers import Controller_Types as CT
from enums.classification import Classification
from service.enum_converter import convert_classification, convert_payment_method
from service.enum_converter import reverse_classification_convert, reverse_payment_method_convert
from service.employee_factory import EmployeeFactory

class EmployeeViewPage(tk.Tk):

    """View Page"""
    def __init__(self, Controller, SearchWindow, employee):
        super().__init__()

        self.geometry("600x400")
        self.title("Employee View")
        self.resizable(0, 0)
        self._SuperController = Controller
        self.__employee = employee
        self.__SearchWindow = SearchWindow
        self.create_str_vars()
        self.create_title_labels()
        self.create_timecard_box()
        self.create_button_str_var()
        self.create_buttom_buttons()
        self.place_title_labels()
        if employee != None:
            self.mode = "view"
            self.create_info_labels()
            self.place_info_labels()
            self.set_values_to_emp(self.__employee)
            self.set_buttons_viewing()
        else:
            self.mode = "add"
            self.create_entry_widgets()
            self.place_entry_widgets()
            self.set_id_for_new_emp()
            self.set_buttons_adding()


    def swap_to_edit(self):
        self.mode = "edit"
        self.destroy_info_labels()
        self.create_entry_widgets()
        self.place_entry_widgets()
        self.set_buttons_editing()

    def swap_to_view(self):
        self.mode = "view"
        self.destroy_entry_widgets()
        self.set_values_to_emp(self.__employee)
        self.create_info_labels()
        self.place_info_labels()
        self.set_buttons_viewing()


    def return_to_search(self):
        self.destroy()

    def create_str_vars(self):
       """Creates labels and boxes for the base view."""

       self.id = tk.StringVar(self, value="")
       self.first_name = tk.StringVar(self, value="")
       self.last_name = tk.StringVar(self, value="")
       self.social_security = tk.StringVar(self, value="")
       self.state = tk.StringVar(self, value="")
       self.city = tk.StringVar(self, value="")
       self.street_address = tk.StringVar(self, value="")
       self.zipcode = tk.StringVar(self, value="")

       self.title = tk.StringVar(self, value="")
       self.department = tk.StringVar(self, value="")
       self.office_email = tk.StringVar(self, value="")
       self.office_phone = tk.StringVar(self, value="")
       self.start_date = tk.StringVar(self, value="")

       self.salary = tk.StringVar(self, value="")
       self.rate = tk.StringVar(self, value="")
       self.route = tk.StringVar(self, value="")
       self.account = tk.StringVar(self, value="")
       self.next_payroll = tk.StringVar(self, value="")
       self.classification = tk.StringVar(self, value="")
       self.payment_method = tk.StringVar(self, value="")

    def set_values_to_emp(self, employee):
        PCon = self._SuperController.get_a_controller(CT.PAYMENT_CONTROLLER)

        self.id.set(employee.id)
        self.first_name.set(employee.first_name)
        self.last_name.set(employee.last_name)
        self.social_security.set(employee.social_security)
        self.state.set(employee.state)
        self.city.set(employee.city)
        self.street_address.set(employee.street_address)
        self.zipcode.set(employee.zipcode)

        self.title.set(employee.title)
        self.department.set(employee.department)
        self.office_email.set(employee.office_email)
        self.office_phone.set(employee.office_phone)
        self.start_date.set(employee.start_date)

        self.salary.set(employee.salary)
        self.rate.set(employee.rate)
        self.route.set(employee.route)
        self.account.set(employee.account)
        self.next_payroll.set("{:.2f}".format(PCon.get_pay(employee.id)))
        self.classification.set(convert_classification(employee.classification))
        self.payment_method.set(convert_payment_method(employee.payment_Method))

    def set_id_for_new_emp(self):
        EmpCon = self._SuperController.get_a_controller(CT.EMPLOYEE_CONTROLLER)
        self.id.set(EmpCon.get_new_employee_id())

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
        self.rate_title_lb = ttk.Label(self, text="Hourly pRate")
        self.route_title_lb = ttk.Label(self, text="Route")
        self.account_title_lb = ttk.Label(self, text="Account")
        self.classification_title_lb = ttk.Label(self, text="Classification")
        self.payment_method_title_lb = ttk.Label(self, text="Payment Method")
        self.next_payroll_title_lb = ttk.Label(self, text="Next Payroll Amount")

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

    def destroy_info_labels(self):
        self.id_lb.destroy()
        self.first_name_lb.destroy()
        self.last_name_lb.destroy()
        self.social_security_lb.destroy()
        self.state_lb.destroy()
        self.city_lb.destroy()
        self.street_address_lb.destroy()
        self.zipcode_lb.destroy()
        self.title_lb.destroy()
        self.department_lb.destroy()
        self.office_email_lb.destroy()
        self.office_phone_lb.destroy()
        self.start_date_lb.destroy()
        self.salary_lb.destroy()
        self.rate_lb.destroy()
        self.route_lb.destroy()
        self.account_lb.destroy()
        self.next_payroll_lb.destroy()
        self.classification_lb.destroy()
        self.payment_method_lb.destroy()

    def create_entry_widgets(self):
        #We'll Consider the Employee ID to be auto-generated, and thus read-only.
        self.id_en = ttk.Label(self, textvariable=self.id)
        self.first_name_en = ttk.Entry(self, textvariable=self.first_name)
        self.last_name_en = ttk.Entry(self, textvariable=self.last_name)
        self.social_security_en = ttk.Entry(self, textvariable=self.social_security)
        self.state_en = ttk.Entry(self, textvariable=self.state)
        self.city_en = ttk.Entry(self, textvariable=self.city)
        self.street_address_en = ttk.Entry(self, textvariable=self.street_address)
        self.zipcode_en = ttk.Entry(self, textvariable=self.zipcode)

        self.title_en = ttk.Entry(self, textvariable=self.title)
        self.department_en = ttk.Entry(self, textvariable=self.department)
        self.office_email_en = ttk.Entry(self, textvariable=self.office_email)
        self.office_phone_en = ttk.Entry(self, textvariable=self.office_phone)
        self.start_date_en = ttk.Entry(self, textvariable=self.start_date)

        self.salary_en = ttk.Entry(self, textvariable=self.salary)
        self.rate_en = ttk.Entry(self, textvariable=self.rate)
        self.route_en = ttk.Entry(self, textvariable=self.route)
        self.account_en = ttk.Entry(self, textvariable=self.account)
        self.next_payroll_en = ttk.Label(self, text="NA")
        self.classification.set("Hourly")
        self.payment_method.set("Mail")
        self.classification_en = ttk.Button(self, textvariable=self.classification, command=self.cycle_classification)
        self.payment_method_en = ttk.Button(self, textvariable=self.payment_method, command=self.cycle_payment_method)


    def cycle_classification(self):
        if self.classification.get() == "Hourly":
            self.classification.set("Commission")
            return None

        if self.classification.get() == "Commission":
            self.classification.set("Salary")
            return None

        if self.classification.get() == "Salary":
            self.classification.set("Hourly")

    def cycle_payment_method(self):
        if self.payment_method.get() == "Mail":
            self.payment_method.set("Direct Deposit")
        else:
            self.payment_method.set("Mail")

    def destroy_entry_widgets(self):
        self.id_en.destroy()
        self.first_name_en.destroy()
        self.last_name_en.destroy()
        self.social_security_en.destroy()
        self.state_en.destroy()
        self.city_en.destroy()
        self.street_address_en.destroy()
        self.zipcode_en.destroy()
        self.title_en.destroy()
        self.department_en.destroy()
        self.office_email_en.destroy()
        self.office_phone_en.destroy()
        self.start_date_en.destroy()
        self.salary_en.destroy()
        self.rate_en.destroy()
        self.route_en.destroy()
        self.account_en.destroy()
        self.next_payroll_en.destroy()
        self.classification_en.destroy()
        self.payment_method_en.destroy()

    def create_button_str_var(self):
        self.left_button_str = tk.StringVar(self, value="Return to Search")
        self.right_button_str = tk.StringVar(self, value="Edit")

    def create_buttom_buttons(self):
        self.left_button = ttk.Button(self, textvariable=self.left_button_str)
        self.right_button = ttk.Button(self, textvariable=self.right_button_str)

    def set_buttons_viewing(self):
        self.left_button_str.set("Return to Search")
        self.right_button_str.set("Edit")
        self.left_button["command"] = self.return_to_search
        self.right_button["command"] = self.swap_to_edit

    def set_buttons_editing(self):
        self.left_button_str.set("Cancel")
        self.right_button_str.set("Save")
        self.left_button["command"] = self.swap_to_view
        self.right_button["command"] = self.attempt_save

    def set_buttons_adding(self):
        self.left_button_str.set("Return to Search")
        self.right_button_str.set("Save")
        self.left_button["command"] = self.return_to_search
        self.right_button["command"] = self.attempt_save


    def create_timecard_box(self):
        self.box_lb = ttk.Label(self, text="Receipts/Timecards - Unadjusted")
        self.receipts_timecards_scrollbox = tk.Scrollbar(self)
        self.the_list_box = tk.Listbox(self)

        if self.__employee == None:
            return None

        if self.__employee.classification == Classification.HOURLY.value:
            TimeCon = self._SuperController.get_a_controller(CT.TIMECARD_CONTROLLER)
            Shifts = TimeCon.get_timecard(self.__employee.id)
            if Shifts == None:
                return None
            for shift in Shifts.hours:
                self.the_list_box.insert(tk.END, shift)

        if self.__employee.classification == Classification.COMMISSIONED.value:
            RecCon = self._SuperController.get_a_controller(CT.RECEIPT_CONTROLLER)
            Fees = RecCon.get_receipt(self.__employee.id)
            if Fees == None:
                return None
            for fee in Fees.costs:
                self.the_list_box.insert(tk.END, fee)


    def place_title_labels(self):
        # PERSONAL INFO #
        self.id_title_lb.grid(column=0, row=0)
        self.first_name_title_lb.grid(column=0, row=1)
        self.last_name_title_lb.grid(column=1, row=1)
        self.social_security_title_lb.grid(column=2, row=0)
        self.state_title_lb.grid(column=0, row=3)
        self.city_title_lb.grid(column=1, row=3)
        self.street_address_title_lb.grid(column=0, row=5)
        self.zipcode_title_lb.grid(column=2, row=3)

        # COMPANY INFO #
        self.title_title_lb.grid(column=0,row=7)
        self.department_title_lb.grid(column=0, row=8)
        self.office_email_title_lb.grid(column=0, row=9)
        self.office_phone_title_lb.grid(column=0, row=10)
        self.start_date_title_lb.grid(column=0, row=11)

        # PAYMENT INFORMATION #
        self.classification_title_lb.grid(column=0, row=12)
        self.payment_method_title_lb.grid(column=0, row=13)
        self.salary_title_lb.grid(column=0, row=14)
        self.rate_title_lb.grid(column=0, row=15)
        self.next_payroll_title_lb.grid(column=0, row=16)
        self.route_title_lb.grid(column=2, row=13)
        self.account_title_lb.grid(column=3, row=13)

        # BOTTOM BUTTONS #
        self.left_button.grid(column=0, row=17)
        self.right_button.grid(column=1, row=17)

        # scrollbar and listbox for the receipts and timecards

        self.box_lb.grid(column=4, row=0)
        self.the_list_box.grid(column=4, rowspan=8, row=1)
        self.receipts_timecards_scrollbox.grid(column=4, rowspan=8, row=1)

    def place_info_labels(self):
        # PERSONAL INFO #
        self.id_lb.grid(column=1, row=0)
        self.first_name_lb.grid(column=0, row=2)
        self.last_name_lb.grid(column=1, row=2)
        self.social_security_lb.grid(column=2, row=1)
        self.state_lb.grid(column=0, row=4)
        self.city_lb.grid(column=1, row=4)
        self.street_address_lb.grid(column=0, row=6)
        self.zipcode_lb.grid(column=2, row=4)

        # COMPANY INFO #
        self.title_lb.grid(column=1, row=7)
        self.department_lb.grid(column=1, row=8)
        self.office_email_lb.grid(column=1, row=9)
        self.office_phone_lb.grid(column=1, row=10)
        self.start_date_lb.grid(column=1, row=11)

        # PAYMENT INFO #
        self.classification_lb.grid(column=1, row=12)
        self.payment_method_lb.grid(column=1, row=13)
        self.salary_lb.grid(column=1, row=14)
        self.rate_lb.grid(column=1, row=15)
        self.next_payroll_lb.grid(column=1, row=16)
        self.route_lb.grid(column=2, row=14)
        self.account_lb.grid(column=3, row=14)

    def place_entry_widgets(self):
        # PERSONAL INFO #
        self.id_en.grid(column=1, row=0)
        self.first_name_en.grid(column=0, row=2)
        self.last_name_en.grid(column=1, row=2)
        self.social_security_en.grid(column=2, row=1)
        self.state_en.grid(column=0, row=4)
        self.city_en.grid(column=1, row=4)
        self.street_address_en.grid(column=0, row=6)
        self.zipcode_en.grid(column=2, row=4)

        # COMPANY INFO #
        self.title_en.grid(column=1, row=7)
        self.department_en.grid(column=1, row=8)
        self.office_email_en.grid(column=1, row=9)
        self.office_phone_en.grid(column=1, row=10)
        self.start_date_en.grid(column=1, row=11)

        # PAYMENT INFO #
        self.classification_en.grid(column=1, row=12)
        self.payment_method_en.grid(column=1, row=13)
        self.salary_en.grid(column=1, row=14)
        self.rate_en.grid(column=1, row=15)
        self.next_payroll_en.grid(column=1, row=16)
        self.route_en.grid(column=2, row=14)
        self.account_en.grid(column=3, row=14)


    def attempt_creation(self):
        Emp_Dict = {
            "id" : self.id.get(),
            "first_name" : self.first_name.get(),
            "last_name" : self.last_name.get(),
            "archived" : False,
            "social_security" : self.social_security.get(),
            "title" : self.title.get(),
            "department" : self.department.get(),
            "office_email" : self.office_email.get(),
            "office_phone" : self.office_phone.get(),
            "start_date" : self.start_date.get(),
            "imported" : False,
            "street_address" : self.street_address.get(),
            "city" : self.city.get(),
            "state" : self.state.get(),
            "zipcode" : self.zipcode.get(),
            "classification" : reverse_classification_convert(self.classification.get()).value,
            "payment_Method" : reverse_payment_method_convert(self.payment_method.get()).value,
            "route" : self.route.get(),
            "account" : self.account.get(),
            "salary" : self.salary.get(),
            "rate" : self.rate.get(),
            "income" : []
        }
        self.potential_employee = EmployeeFactory.create_employee("add_screen", Emp_Dict)

    def attempt_save(self):
        self.attempt_creation()
        if self.potential_employee.valid:
            self.__employee = self.potential_employee
            EmpCon = self._SuperController.get_a_controller(CT.EMPLOYEE_CONTROLLER)
            EmpCon.update_employee(self.__employee)
            self.__SearchWindow.get_emp_dict()
        self.save_wrap_up(self.potential_employee.valid)

    def save_wrap_up(self, result):
        if self.mode == "edit" and result:
            self.swap_to_view()
        if self.mode == "add" and result:
            self.return_to_search()
