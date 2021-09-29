import tkinter as tk
from tkinter import ttk


class EmployeeSearchPage(tk.Tk):
    """Search Page """
    def __init__(self):
        super().__init__()

        self.geometry("550x250")
        self.title('Employee Search')
        self.resizable(0, 0)

        # grid config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.create_widgets()

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
        self.left_list_box = tk.Listbox(self)
        self.left_list_box.grid(column=0, row=2)
        for stuff in range(1, 100):
            self.left_list_box.insert(stuff, f"TEST {stuff}")

        # scroll bar for left side list box
        left_scrollbar = tk.Scrollbar(self)
        left_scrollbar.grid(column=0, row=2, sticky="NSE")
        left_scrollbar.config(command=self.left_list_box.yview)

        # add button
        add_button = ttk.Button(self, text="Add->")
        add_button.grid(column=1, row=1, sticky="N")

        # remove Button
        remove_button = ttk.Button(self, text="<-Remove")
        remove_button.grid(column=1, row=2, sticky="S")

        # right list box
        self.right_list_box = tk.Listbox(self)
        self.right_list_box.grid(column=2, row=2, sticky="NS")

        # scroll bar for right side list box
        right_scrollbar = tk.Scrollbar(self)
        right_scrollbar.grid(column=2, row=2, stick="NSE")
        right_scrollbar.config(command=self.right_list_box.yview)

        # view employee button
        view_button = ttk.Button(self, text="View\nEmployee")
        view_button.grid(column=3, row=1, sticky="N", padx=40)

        # pay button
        pay_button = ttk.Button(self, text="Pay\nEmployees")
        pay_button.grid(column=3, row=2, sticky="S", padx=30)

        # close button
        close_button = ttk.Button(self, text="Close")
        close_button.grid(column=3, row=2, padx=30)
        
        # logout button
        logout_button = ttk.Button(self, text="Logout")
        logout_button.grid(column=3, row=2, sticky="N", pady=30)




def main():
    app = EmployeeSearchPage()
    app.mainloop()


if __name__ == "__main__":
    main()

