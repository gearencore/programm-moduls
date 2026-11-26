import tkinter as tk
import math

root = tk.Tk()
root.title("Узор из кнопок")
root.geometry("350x350")

i = 0

while i < 12:
    x = 150 + 110 * math.sin(i * math.pi / 6)
    y = 150 - 110 * math.cos(i * math.pi / 6)

    btn = tk.Button(root, text=str(i + 1), width=4, height=2)
    btn.place(x=x, y=y)

    i += 1

root.mainloop()
