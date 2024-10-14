import tkinter as tk
from tkinter import messagebox

def check_brackets(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return not stack

def evaluate_expression():
    expression = entry_expression.get()

    if not expression:
        messagebox.showerror("Input Error", "Please enter an expression.")
        return
    
    result_label.config(text="")
    
    if not check_brackets(expression):
        result_label.config(text="Error: Invalid bracket arrangement.")
        return
    
    expression = expression.replace('[', '(').replace(']', ')')
    expression = expression.replace('{', '(').replace('}', ')')
    
    try:
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

r = tk.Tk()
r.title('Bracket and Expression Validator')
r.geometry('500x250')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_expression = tk.Label(r, text="Enter the arithmetic expression:")
label_expression.pack()
entry_expression = tk.Entry(r, width=50)
entry_expression.pack()

button_evaluate = tk.Button(r, text='Evaluate Expression', width=25, command=evaluate_expression)
button_evaluate.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
