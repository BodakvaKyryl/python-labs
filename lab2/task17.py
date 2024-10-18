import tkinter as tk
from tkinter import messagebox

def change_theme():
	if root["bg"] == light_bg:
		root.config(bg=dark_root_bg)
		general_info_label.config(bg=dark_bg, fg=dark_fg)
		task_sentence_label.config(bg=dark_bg, fg=dark_fg)
		entry_sentence.config(bg=dark_entry_bg, fg=dark_fg, insertbackground=dark_fg)
		result_label.config(bg=dark_bg, fg=dark_fg)
		count_button.config(bg=dark_button_bg, fg=dark_button_fg)
		theme_button.config(bg=dark_button_bg, fg=dark_button_fg, text="Light Mode")
	else:
		root.config(bg=light_bg)
		general_info_label.config(bg=light_bg, fg=light_fg)
		task_sentence_label.config(bg=light_bg, fg=light_fg)
		entry_sentence.config(bg=light_entry_bg, fg=light_fg, insertbackground=light_fg)
		result_label.config(bg=light_bg, fg=light_fg)
		count_button.config(bg=light_button_bg, fg=light_button_fg)
		theme_button.config(bg=light_button_bg, fg=light_button_fg, text="Dark Mode")

def count_letters():
	sentence = entry_sentence.get().lower()
	vowels = "aeiou"
	consonants = "bcdfghjklmnpqrstvwxyz"

	vowel_count = sum(1 for letter in sentence if letter in vowels)
	consonant_count = sum(1 for letter in sentence if letter in consonants)

	result_label.config(text=f"Vowels: {vowel_count}, Consonants: {consonant_count}")

light_bg = "#ffffff"
light_fg = "#000000"
light_entry_bg = "#f0f0f0"
light_button_bg = "#d0d0d0"
light_button_fg = "#000000"
dark_root_bg = "#2c2c2c"
dark_bg = "#3D3D3D"
dark_fg = "#ffffff"
dark_entry_bg = "#3d3d3d"
dark_button_bg = "#444444"
dark_button_fg = "#ffffff"

root = tk.Tk()
root.geometry("1000x300")
root.title("Vowel and Consonant Counter")
root.config(bg=dark_root_bg)

general_info = '''
Інформація про автора ПЗ:
ВНЗ: "Київський політехнічний інститут імені Ігоря Сікорського"
Кафедра: Програмного забезпечення комп'ютерних систем
Факультет: Факультет прикладної математики
група: КП-11
ПІБ: Бодаква Кирил
Опис ПЗ:
The software counts the number of vowels and consonants in the entered sentence
'''
general_info_label = tk.Label(root, text=general_info, font=("Arial", 10),
justify="left", bg=dark_bg, fg=dark_fg)
general_info_label.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)

task_sentence_label = tk.Label(root, text="Enter a sentence:", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
task_sentence_label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

entry_sentence = tk.Entry(root, width=50, font=("Arial", 12), justify="center", bg=dark_entry_bg, fg=dark_fg)
entry_sentence.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

count_button = tk.Button(root, text="Count Letters", font=("Arial", 12), command=count_letters, bg=dark_button_bg, fg=dark_button_fg)
count_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

theme_button = tk.Button(root, text="Light Mode", font=("Arial", 12), command=change_theme, bg=dark_button_bg, fg=dark_button_fg)
theme_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
result_label.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure([0, 1, 2, 3], weight=1)

root.mainloop()
