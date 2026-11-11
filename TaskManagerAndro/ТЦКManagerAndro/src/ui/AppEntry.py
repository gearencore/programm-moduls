
import tkinter as tk


class AppEntry(tk.Entry):
    def __init__(self, master):
        super().__init__(master, font=('Arial', 12), bg='#303030',
                         fg='white', insertbackground='white')
