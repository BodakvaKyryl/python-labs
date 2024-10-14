import tkinter as tk
from collections import Counter
from tkinter import messagebox

def find_most_frequent_char():
    text = entry_text.get()

    if not text:
        messagebox.showerror("Input Error", "Please enter some text.")
        return

    char_count = Counter(text)

    most_frequent_char = max(char_count, key=char_count.get)
    frequency = char_count[most_frequent_char]

    result_label.config(text=f"Most frequent character: '{most_frequent_char}' with {frequency} occurrences.")

r = tk.Tk()
r.title('Most Frequent Character Finder')
r.geometry('500x200')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_text = tk.Label(r, text="Enter the text:")
label_text.pack()
entry_text = tk.Entry(r, width=50)
entry_text.pack()

button_find = tk.Button(r, text='Find Most Frequent Character', width=25, command=find_most_frequent_char)
button_find.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
