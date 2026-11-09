"""Переиспользуемая надпись интерфейса Task Manager."""
import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, master, text):
        super().__init__(
            master, text=text, font=('Arial', 18, 'bold'),
            bg='#202020', fg='white'
        )
