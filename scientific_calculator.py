import tkinter as tk
import math

# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x500")
root.resizable(False, False)

# -------------------------------
# Equation Display (Screen)
# -------------------------------
display = tk.Entry(root, font=("Arial", 22), bd=10, relief=tk.RIDGE, justify="right")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=20, ipadx=8, ipady=15)

# -------------------------------
# Button Click Function
# -------------------------------
def click(value):
    display.insert(tk.END, value)

# -------------------------------
# Clear Screen
# -------------------------------
def clear():
    display.delete(0, tk.END)

# -------------------------------
# Calculate Result
# -------------------------------
def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# -------------------------------
# Scientific Functions
# -------------------------------
def sqrt():
    try:
        value = float(display.get())
        result = math.sqrt(value)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.insert(0, "Error")

def square():
    try:
        value = float(display.get())
        result = value ** 2
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.insert(0, "Error")

def sin():
    try:
        value = float(display.get())
        result = math.sin(math.radians(value))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.insert(0, "Error")

def cos():
    try:
        value = float(display.get())
        result = math.cos(math.radians(value))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.insert(0, "Error")

def tan():
    try:
        value = float(display.get())
        result = math.tan(math.radians(value))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.insert(0, "Error")

# -------------------------------
# Buttons Layout
# -------------------------------
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('√',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('x²',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('sin',3,4),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), ('cos',4,4),
    ('C',5,0), ('tan',5,1)
]

# -------------------------------
# Button Creation
# -------------------------------
for (text, row, col) in buttons:
    if text == "=":
        command = calculate
    elif text == "C":
        command = clear
    elif text == "√":
        command = sqrt
    elif text == "x²":
        command = square
    elif text == "sin":
        command = sin
    elif text == "cos":
        command = cos
    elif text == "tan":
        command = tan
    else:
        command = lambda t=text: click(t)

    tk.Button(root, text=text, width=6, height=2,
              font=("Arial", 14),
              command=command).grid(row=row, column=col, padx=5, pady=5)

# -------------------------------
# Run Application
# -------------------------------
root.mainloop()
