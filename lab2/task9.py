import os
import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse

def change_theme():
    if root["bg"] == light_bg:
        root.config(bg=dark_root_bg)
        general_info_label.config(bg=dark_bg, fg=dark_fg)
        task_label.config(bg=dark_bg, fg=dark_fg)
        entry_url.config(bg=dark_entry_bg, fg=dark_fg, insertbackground=dark_fg)
        result_label.config(bg=dark_bg, fg=dark_fg)
        analyze_button.config(bg=dark_button_bg, fg=dark_button_fg)
        theme_button.config(bg=dark_button_bg, fg=dark_button_fg, text="Light Mode")
    else:
        root.config(bg=light_bg)
        general_info_label.config(bg=light_bg, fg=light_fg)
        task_label.config(bg=light_bg, fg=light_fg)
        entry_url.config(bg=light_entry_bg, fg=light_fg, insertbackground=light_fg)
        result_label.config(bg=light_bg, fg=light_fg)
        analyze_button.config(bg=light_button_bg, fg=light_button_fg)
        theme_button.config(bg=light_button_bg, fg=light_button_fg, text="Dark Mode")

def analyze_url():
    url = entry_url.get()

    if not url:
        messagebox.showerror("Input Error", "Please enter a valid URL.")
        return

    try:
        parsed_url = urlparse(url)
        
        protocol = parsed_url.scheme
        domain = parsed_url.hostname
        path = parsed_url.path
        
        if domain:
            domain_parts = domain.split('.')
            if len(domain_parts) > 2:
                subdomain = '.'.join(domain_parts[:-2])
                domain_name = domain_parts[-2]
                domain_zone = domain_parts[-1]
            else:
                subdomain = ''
                domain_name = domain_parts[-2] if len(domain_parts) > 1 else domain_parts[0]
                domain_zone = domain_parts[-1] if len(domain_parts) > 1 else ''
        else:
            subdomain = domain_name = domain_zone = ''
        
        directory, file_name = os.path.split(path)
        depth = len(directory.strip('/').split('/')) if directory else 0
        
        result = f"Protocol: {protocol}\n"
        result += f"Domain: {domain_name}\n"
        result += f"Domain Zone: {domain_zone}\n"
        result += f"Subdomain: {subdomain if subdomain else 'None'}\n"
        result += f"Subdirectory: {directory if directory else 'None'}\n"
        result += f"Depth: {depth}\n"
        result += f"File Name: {file_name if file_name else 'None'}"
        
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid URL or Error: {e}")

def enable_paste(event):
    entry_url.event_generate('<<Paste>>')

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
root.title("URL Analyzer")
root.config(bg=dark_root_bg)

general_info = '''
Інформація про автора ПЗ:
ВНЗ: "Київський політехнічний інститут імені Ігоря Сікорського"
Кафедра: Програмного забезпечення комп'ютерних систем
Факультет: Факультет прикладної математики
група: КП-11
ПІБ: Бодаква Кирил
Опис ПЗ:
URL analyzer
'''
general_info_label = tk.Label(root, text=general_info, font=("Arial", 10),
justify="left", bg=dark_bg, fg=dark_fg)
general_info_label.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)

task_label = tk.Label(root, text="Enter a URL:", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
task_label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

entry_url = tk.Entry(root, width=50, font=("Arial", 12), justify="center", bg=dark_entry_bg, fg=dark_fg)
entry_url.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
entry_url.bind('<Control-v>', enable_paste)

analyze_button = tk.Button(root, text="Analyze URL", font=("Arial", 12), command=analyze_url, bg=dark_button_bg, fg=dark_button_fg)
analyze_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

theme_button = tk.Button(root, text="Light Mode", font=("Arial", 12), command=change_theme, bg=dark_button_bg, fg=dark_button_fg)
theme_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
result_label.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure([0, 1, 2, 3], weight=1)

root.mainloop()
