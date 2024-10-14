import tkinter as tk
from tkinter import messagebox
import re

def count_common_words():
    sentence1 = entry_sentence1.get()
    sentence2 = entry_sentence2.get()

    if not sentence1 or not sentence2:
        messagebox.showerror("Input Error", "Please enter both sentences.")
        return

    words1 = set(re.findall(r'\b\w+\b', sentence1.lower()))
    words2 = set(re.findall(r'\b\w+\b', sentence2.lower()))

    common_words = words1.intersection(words2)
    count = len(common_words)

    result_label.config(text=f"{count} words from the first sentence are in the second.")

r = tk.Tk()
r.title('Common Words Counter')
r.geometry('500x400')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_sentence1 = tk.Label(r, text="Enter the first sentence:")
label_sentence1.pack()
entry_sentence1 = tk.Entry(r, width=50)
entry_sentence1.pack()

label_sentence2 = tk.Label(r, text="Enter the second sentence:")
label_sentence2.pack()
entry_sentence2 = tk.Entry(r, width=50)
entry_sentence2.pack()

button_count = tk.Button(r, text='Count', width=9, command=count_common_words)
button_count.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
