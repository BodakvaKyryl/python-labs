import tkinter as tk
from tkinter import messagebox

def count_occurrences():
    sequence = entry_sequence.get()
    symbol = entry_symbol.get()
    
    if len(symbol) != 1:
        messagebox.showerror("Input Error", "Please enter a single character for symbol.")
        return

    count = sequence.count(symbol)
    result_label.config(text=f"The symbol '{symbol}' appears {count} times.")

r = tk.Tk()
r.title('Symbol Counter')
r.geometry('500x400+20+20')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_sequence = tk.Label(r, text="Enter a sequence of characters:")
label_sequence.pack()
entry_sequence = tk.Entry(r, width=50)
entry_sequence.pack()

label_symbol = tk.Label(r, text="Enter a symbol to count:")
label_symbol.pack()
entry_symbol = tk.Entry(r, width=10)
entry_symbol.pack()

button_count = tk.Button(r, text='Count', width=9, command=count_occurrences)
button_count.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
