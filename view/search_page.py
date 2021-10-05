import tkinter as tk
from tkinter import ttk
from controller.user_controller import UserController


class EmployeeSearchPage(tk.Tk):
    """Search Page """
    def __init__(self):
        super().__init__()

        self.geometry("550x250")
        self.title('Employee Search')
        self.resizable(0, 0)
        self.UC = UserController.get_controller()
        # grid config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.create_widgets()

    def move_items_lr(self):
        curr = self.left_list_box.curselection()
        self.left_list_box.selection_clear(0, self.left_list_box.size())
        for index in curr:
            self.right_list_box.insert(tk.END, self.left_list_box.get(index))
            self.left_list_box.delete(index)

    def move_items_rl(self):
        curr = self.right_list_box.curselection()
        self.right_list_box.selection_clear(0, self.right_list_box.size())
        for index in curr:
            self.left_list_box.insert(tk.END, self.right_list_box.get(index))
            self.right_list_box.delete(index)

    #We'll use in combination with "Select All"
    def fill_side(self, side):
        for index, emp in enumerate(self.emp_dict):
            side.insert(index, emp)

    def clear_side(self, side):
       side.delete(0, tk.END)

    def select_all(self):
        self.clear_side(self.left_list_box)
        self.clear_side(self.right_list_box)
        self.fill_side(self.right_list_box)

    def reset(self):
        self.clear_side(self.left_list_box)
        self.clear_side(self.right_list_box)
        self.fill_side(self.left_list_box)

    def do_payroll(self):
        names = self.right_list_box.get(0,tk.END)
        id_list = [self.emp_dict.get(name) for name in names]
        self.UC.make_payroll(id_list)

    def create_widgets(self):
        """Create widgets for Employee Search Page"""

        # search label
        search_label = ttk.Label(self, text="Search")
        search_label.grid(column=0, row=0)

        # search box
        self.search_box = tk.StringVar(value="")
        username_entry = ttk.Entry(self, textvariable=self.search_box)
        username_entry.grid(column=0, row=1)

        # left side list box
        self.left_list_box = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.left_list_box.grid(column=0, row=2)

        # right list box
        self.right_list_box = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.right_list_box.grid(column=2, row=2, sticky="NS")

        # Test example to populate the left side list box!!!
        self.emp_dict = self.UC.get_employee_dict()
        self.fill_side(self.left_list_box)

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
        view_button = ttk.Button(self, text="View\nEmployee")
        view_button.grid(column=3, row=1, sticky="N", padx=40)

        # pay button
        pay_button = ttk.Button(self, text="Pay\nEmployees", command=self.do_payroll)
        pay_button.grid(column=3, row=2, sticky="S", padx=30)

        # close button
        close_button = ttk.Button(self, text="Close")
        close_button.grid(column=3, row=2, padx=30)

        # logout button
        logout_button = ttk.Button(self, text="Logout")
        logout_button.grid(column=3, row=2, sticky="N", pady=30)




def main():
    UC = UserController.start_controller()
    UC.login_bypass()
    app = EmployeeSearchPage()
    app.mainloop()


if __name__ == "__main__":
    main()
