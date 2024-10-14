import tkinter as tk
from tkinter import messagebox
import re

def find_shortest_word_length():
    sentence = entry_sentence.get()

    if not sentence:
        messagebox.showerror("Input Error", "Please enter a sentence.")
        return

    words = re.findall(r'\b\w+\b', sentence)

    if not words:
        messagebox.showerror("Input Error", "No words found in the sentence.")
        return

    shortest_word_length = min(len(word) for word in words)

    result_label.config(text=f"The shortest word length is: {shortest_word_length}")

r = tk.Tk()
r.title('Shortest Word Finder')
r.geometry('500x200')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_sentence = tk.Label(r, text="Enter a sentence:")
label_sentence.pack()
entry_sentence = tk.Entry(r, width=50)
entry_sentence.pack()

button_find = tk.Button(r, text='Find Shortest Word', width=20, command=find_shortest_word_length)
button_find.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
