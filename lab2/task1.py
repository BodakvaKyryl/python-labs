import tkinter as tk
from tkinter import messagebox

def change_theme():
	if root["bg"] == light_bg:
		root.config(bg=dark_root_bg)
		general_info_label.config(bg=dark_bg, fg=dark_fg)
		task_sequence_label.config(bg=dark_bg, fg=dark_fg)
		task_symbol_label.config(bg=dark_bg, fg=dark_fg)
		entry_sequence.config(bg=dark_entry_bg, fg=dark_fg, insertbackground=dark_fg)
		entry_symbol.config(bg=dark_entry_bg, fg=dark_fg, insertbackground=dark_fg)
		result_label.config(bg=dark_bg, fg=dark_fg)
		format_button.config(bg=dark_button_bg, fg=dark_button_fg)
		theme_button.config(bg=dark_button_bg, fg=dark_button_fg, text="Light Mode")
	else:
		root.config(bg=light_bg)
		general_info_label.config(bg=light_bg, fg=light_fg)
		task_sequence_label.config(bg=light_bg, fg=light_fg)
		task_symbol_label.config(bg=light_bg, fg=light_fg)
		entry_sequence.config(bg=light_entry_bg, fg=light_fg, insertbackground=light_fg)
		entry_symbol.config(bg=light_entry_bg, fg=light_fg, insertbackground=light_fg)
		result_label.config(bg=light_bg, fg=light_fg)
		format_button.config(bg=light_button_bg, fg=light_button_fg)
		theme_button.config(bg=light_button_bg, fg=light_button_fg, text="Dark Mode")

def count_occurrences():
	sequence = entry_sequence.get()
	symbol = entry_symbol.get()
	
	if len(symbol) != 1:
		messagebox.showerror("Input Error", "Please enter a single character for symbol.")
		return

	count = sequence.count(symbol)
	result_label.config(text=f"The symbol '{symbol}' appears {count} times.")

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
root.geometry("1000x400")
root.title("Symbol Occurrence Counter")
root.config(bg=dark_root_bg)

general_info = '''
Інформація про автора ПЗ:
ВНЗ: "Київський політехнічний інститут імені Ігоря Сікорського"
Кафедра: Програмного забезпечення комп'ютерних систем
Факультет: Факультет прикладної математики
група: КП-11
ПІБ: Бодаква Кирил
Опис ПЗ:
The software counts the number of occurrences of the specified symbol in the entered sequence
'''
general_info_label = tk.Label(root, text=general_info, font=("Arial", 10),
justify="left", bg=dark_bg, fg=dark_fg)
general_info_label.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)

task_sequence_label = tk.Label(root, text="Enter a sequence:", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
task_sequence_label.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

entry_sequence = tk.Entry(root, width=30, font=("Arial", 12), justify="center", bg=dark_entry_bg, fg=dark_fg)
entry_sequence.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

task_symbol_label = tk.Label(root, text="Enter a symbol:", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
task_symbol_label.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

entry_symbol = tk.Entry(root, width=5, font=("Arial", 12), justify="center", bg=dark_entry_bg, fg=dark_fg)
entry_symbol.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

format_button = tk.Button(root, text="Count Occurrences", font=("Arial", 12), command=count_occurrences, bg=dark_button_bg, fg=dark_button_fg)
format_button.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)

theme_button = tk.Button(root, text="Light Mode", font=("Arial", 12), command=change_theme, bg=dark_button_bg, fg=dark_button_fg)
theme_button.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
result_label.grid(row=5, column=1, sticky="nsew", padx=10, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

root.mainloop()
