import tkinter as tk
from tkinter import messagebox
import re

def round_numbers_in_sequence():
    sequence = entry_sequence.get()

    if not sequence:
        messagebox.showerror("Input Error", "Please enter a sequence.")
        return

    def round_match(match):
        number = float(match.group())
        return f"{number:.2f}"

    new_sequence = re.sub(r'\d+\.\d+', round_match, sequence)

    result_label.config(text=f"New sequence: {new_sequence}")

r = tk.Tk()
r.title('Number Rounding in Sequence')
r.geometry('500x200')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_sequence = tk.Label(r, text="Enter the sequence:")
label_sequence.pack()
entry_sequence = tk.Entry(r, width=50)
entry_sequence.pack()

button_round = tk.Button(r, text='Round Numbers', width=20, command=round_numbers_in_sequence)
button_round.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
