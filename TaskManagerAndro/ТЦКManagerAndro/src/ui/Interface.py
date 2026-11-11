import tkinter as tk
from tkinter import messagebox

from ui.AppLabel import AppLabel
from ui.AppListbox import AppListbox
from ui.AppEntry import AppEntry
from ui.Button import AppButton


class Interface:
    def __init__(self, width=650, height=680):
        self.root = tk.Tk()
        self.root.title('Task Manager')
        self.root.geometry(f'{width}x{height}')
        self.root.minsize(480, 520)
        self.root.configure(bg='#202020')

    def label(self, master, text):
        return AppLabel(master, text)

    def listbox(self, master):
        return AppListbox(master)

    def entry(self, master):
        return AppEntry(master)

    def button(self, master, text, command):
        return AppButton(master, text, command)

    def warning(self, title, text):
        messagebox.showwarning(title, text, parent=self.root)

    def error(self, title, text):
        messagebox.showerror(title, text, parent=self.root)

    def confirm(self, title, text):
        return messagebox.askyesno(title, text, parent=self.root)
