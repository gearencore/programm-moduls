
import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("290x340")
root.resizable(False, False)

expression = ""

text_input = tk.Label(
    root,
    text="0",
    font=("Arial", 18),
    bg="white",
    width=19,
    height=2,
    anchor="e",
    relief="sunken"
)
text_input.grid(row=0, column=0, columnspan=4, padx=10, pady=15)


def update_label():
    if expression == "":
        text_input.config(text="0")
    else:
        text_input.config(text=expression)


def click_number(number):
    global expression
    expression += str(number)
    update_label()


def click_operator(op):
    global expression

    if op == "=":
        if expression == "":
            text_input.config(text="Ошибка")
        else:
            try:
                if expression[-1] in "+-*%":
                    text_input.config(text="Ошибка")
                else:
                    result = eval(expression)
                    expression = str(result)
                    update_label()
            except:
                expression = ""
                text_input.config(text="Ошибка")

    else:
        if expression == "":
            if op == "-":
                expression = "-"
        else:
            if expression[-1] in "+-*%":
                expression = expression[:-1] + op
            else:
                expression += op

        update_label()


def clear():
    global expression
    expression = ""
    update_label()


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

row = 1
column = 0

for num in numbers:
    btn = tk.Button(
        root,
        text=str(num),
        width=6,
        height=2,
        font=("Arial", 11),
        command=lambda n=num: click_number(n)
    )

    if num == 0:
        btn.grid(row=4, column=1, padx=3, pady=4)
    else:
        btn.grid(row=row, column=column, padx=3, pady=4)
        column += 1

        if column == 3:
            column = 0
            row += 1


operations = ["*", "%", "+", "-", "="]

for i in range(5):
    btn = tk.Button(
        root,
        text=operations[i],
        width=6,
        height=2,
        font=("Arial", 11),
        command=lambda op=operations[i]: click_operator(op)
    )
    btn.grid(row=i + 1, column=3, padx=3, pady=4)


btn_clear = tk.Button(
    root,
    text="C",
    width=6,
    height=2,
    font=("Arial", 11),
    command=clear
)
btn_clear.grid(row=4, column=0, padx=3, pady=4)

root.mainloop()
