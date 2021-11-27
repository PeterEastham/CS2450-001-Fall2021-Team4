"""
Using this as a decorator to certain functions.
Creates a "pop-up" window that disables the underlying window.
Useful for Permission Handling.
"""
import tkinter as tk
from tkinter import ttk


class Notification(tk.Tk):

    def __init__(self, message, calledWindow):
        super().__init__()
        calledWindow.toggle_window_disable()
        self.__calledWindow = calledWindow

        self.geometry("400x100")
        self.title("Notice")
        self.resizable(0, 0)
        self.rowconfigure(0, weight=3)
        self.columnconfigure(0, weight=2)
        self.message = ttk.Label(self, text=message)
        self.message.grid(column=0, row=0, columnspan=2, ipady=30)

        self.button = ttk.Button(self, text="I Understand", command=self.handle_close)
        self.button.grid(column=1, row=1, padx=10, pady=10)

        self.protocol("WM_DELETE_WINDOW", self.handle_close)



    def handle_close(self):
        self.__calledWindow.toggle_window_disable()
        self.destroy()
