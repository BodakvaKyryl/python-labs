import tkinter as tk
from tkinter import messagebox

def find_common_letters():
    word1 = entry_word1.get().lower()
    word2 = entry_word2.get().lower()
    word3 = entry_word3.get().lower()

    if not word1 or not word2 or not word3:
        messagebox.showerror("Input Error", "Please enter all three words.")
        return

    set1 = set(word1)
    set2 = set(word2)
    set3 = set(word3)

    common_letters = set1 & set2 & set3

    if common_letters:
        result_label.config(text=f"Common letters: {', '.join(sorted(common_letters))}")
    else:
        result_label.config(text="No common letters found.")

r = tk.Tk()
r.title('Common Letters Finder')
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

label_word3 = tk.Label(r, text="Enter the third word:")
label_word3.pack()
entry_word3 = tk.Entry(r, width=50)
entry_word3.pack()

button_find = tk.Button(r, text='Find Common Letters', width=20, command=find_common_letters)
button_find.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
