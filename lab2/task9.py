import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse
import os

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

r = tk.Tk()
r.title('URL Analyzer')
r.geometry('500x400')

studentInfo = tk.Label(r, text="Student K.I. Bodakva\nKPI, PZKS")
studentInfo.pack()

label_url = tk.Label(r, text="Enter the URL:")
label_url.pack()
entry_url = tk.Entry(r, width=50)
entry_url.pack()

button_analyze = tk.Button(r, text='Analyze URL', width=20, command=analyze_url)
button_analyze.pack()

button_exit = tk.Button(r, text='Exit', width=9, command=r.destroy)
button_exit.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()
