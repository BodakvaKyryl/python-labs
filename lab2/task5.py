import tkinter as tk
from tkinter import messagebox
from collections import Counter

def check_anagram():
    word1 = entry_word1.get().lower()
    word2 = entry_word2.get().lower()

    if not word1 or not word2:
        messagebox.showerror("Input Error", "Please enter both words.")
        return

    can_form_simple = set(word2).issubset(set(word1))

    can_form_exact = Counter(word2) <= Counter(word1)
    
    result = ""
    if can_form_simple:
        result += "First word can form the second (ignoring repeats).\n"
    else:
        result += "First word cannot form the second (ignoring repeats).\n"
    
    if can_form_exact:
        result += "First word can form the second (exact counts).\n"
    else:
        result += "First word cannot form the second (exact counts).\n"

    result_label.config(text=result)

r = tk.Tk()
r.title('Word Formation Checker')
r.geometry('500x300')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_word1 = tk.Label(r, text="Enter the first word:")
label_word1.pack()
entry_word1 = tk.Entry(r, width=50)
entry_word1.pack()

label_word2 = tk.Label(r, text="Enter the second word:")
label_word2.pack()
entry_word2 = tk.Entry(r, width=50)
entry_word2.pack()

button_check = tk.Button(r, text='Check Words', width=20, command=check_anagram)
button_check.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
