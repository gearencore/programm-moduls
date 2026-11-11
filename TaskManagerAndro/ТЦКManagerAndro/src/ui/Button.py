import tkinter as tk


class AppButton(tk.Button):
    def __init__(self, master, text, command):
        super().__init__(master, text=text, command=command)
