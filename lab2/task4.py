import tkinter as tk
from tkinter import messagebox

def find_longest_repeated_sequence():
    sentence = entry_sentence.get()

    if not sentence:
        messagebox.showerror("Input Error", "Please enter a sentence.")
        return

    max_char = ''
    max_length = 0
    current_char = ''
    current_length = 0

    for char in sentence:
        if char == current_char:
            current_length += 1
        else:
            current_char = char
            current_length = 1

        if current_length > max_length:
            max_length = current_length
            max_char = current_char

    if max_length > 0:
        result_label.config(text=f"Symbol: '{max_char}', Length: {max_length}")
    else:
        result_label.config(text="No repeated symbols found.")

r = tk.Tk()
r.title('Longest Repeated Symbol Finder')
r.geometry('500x200')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_sentence = tk.Label(r, text="Enter a sentence:")
label_sentence.pack()
entry_sentence = tk.Entry(r, width=50)
entry_sentence.pack()

button_find = tk.Button(r, text='Find Longest Sequence', width=20, command=find_longest_repeated_sequence)
button_find.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
