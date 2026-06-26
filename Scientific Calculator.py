import tkinter as tk
import math

# -----------------------
# Scientific Calculator
# Author: dhiraj7kr

"""
Scientific Calculator
Author: dhiraj7kr
Version: 1.0
Language: Python 3
Description: A GUI-based scientific calculator built using Tkinter.
"""
# -----------------------

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x650")
root.resizable(False, False)

expression = ""

# Display
display = tk.Entry(
    root,
    font=("Arial", 22),
    bd=10,
    relief=tk.GROOVE,
    justify="right"
)
display.pack(fill="both", padx=10, pady=10, ipady=15)

# -----------------------
# Functions
# -----------------------

def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def backspace():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def calculate():
    global expression
    try:
        expr = expression

        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("e", str(math.e))
        expr = expr.replace("^", "**")

        result = eval(expr)

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

def sqrt():
    global expression
    try:
        result = math.sqrt(float(eval(expression)))
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

def sin():
    global expression
    try:
        result = math.sin(math.radians(float(eval(expression))))
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def cos():
    global expression
    try:
        result = math.cos(math.radians(float(eval(expression))))
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def tan():
    global expression
    try:
        result = math.tan(math.radians(float(eval(expression))))
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def log():
    global expression
    try:
        result = math.log10(float(eval(expression)))
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def ln():
    global expression
    try:
        result = math.log(float(eval(expression)))
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def factorial():
    global expression
    try:
        result = math.factorial(int(eval(expression)))
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# -----------------------
# Buttons
# -----------------------

frame = tk.Frame(root)
frame.pack()

buttons = [
    ("7", lambda: press("7")),
    ("8", lambda: press("8")),
    ("9", lambda: press("9")),
    ("/", lambda: press("/")),
    ("√", sqrt),

    ("4", lambda: press("4")),
    ("5", lambda: press("5")),
    ("6", lambda: press("6")),
    ("*", lambda: press("*")),
    ("xʸ", lambda: press("^")),

    ("1", lambda: press("1")),
    ("2", lambda: press("2")),
    ("3", lambda: press("3")),
    ("-", lambda: press("-")),
    ("%", lambda: press("/100")),

    ("0", lambda: press("0")),
    (".", lambda: press(".")),
    ("=", calculate),
    ("+", lambda: press("+")),
    ("C", clear),

    ("sin", sin),
    ("cos", cos),
    ("tan", tan),
    ("log", log),
    ("ln", ln),

    ("π", lambda: press("π")),
    ("e", lambda: press("e")),
    ("(", lambda: press("(")),
    (")", lambda: press(")")),
    ("n!", factorial),

    ("⌫", backspace),
]

row = 0
col = 0

for (text, cmd) in buttons:
    b = tk.Button(
        frame,
        text=text,
        command=cmd,
        width=8,
        height=3,
        font=("Arial", 14),
        bg="#f2f2f2"
    )
    b.grid(row=row, column=col, padx=3, pady=3)

    col += 1
    if col == 5:
        col = 0
        row += 1

root.mainloop()
