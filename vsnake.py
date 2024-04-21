# Tech@JesseJesse.com
import tkinter as tk
import subprocess
import pyperclip
import os
import webbrowser
import threading
import platform

def download_video():
    url = url_entry.get()
    if url:
        threading.Thread(target=download_video_thread, args=(url,), daemon=True).start()

def download_video_thread(url):
    process = subprocess.Popen(['yt-dlp', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    root.after(0, lambda: update_terminal(out, err))
    root.after(0, lambda: update_footer())

def update_terminal(out, err):
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END)
    terminal_output.insert(tk.END, out.decode("utf-8"))
    terminal_output.insert(tk.END, err.decode("utf-8"))
    terminal_output.config(state=tk.DISABLED)

def paste_from_clipboard():
    clipboard_text = pyperclip.paste()
    url_entry.delete(0, tk.END)
    url_entry.insert(0, clipboard_text)
    url_entry.config(fg='white')

def clear_url_entry(event=None):
    url_entry.delete(0, tk.END)
    url_entry.config(fg='white')

def on_focus_in(event):
    if url_entry.get() == "Enter the full URL https://":
        url_entry.delete(0, tk.END)
        url_entry.config(fg='white')

def on_focus_out(event):
    if not url_entry.get():
        url_entry.insert(0, "Enter the full URL https://")
        url_entry.config(fg='gray')

def quit_program():
    os.kill(os.getpid(), 2)

def install_youtube_dl():
    subprocess.Popen(['brew', 'install', 'youtube-dl'])

def open_help_popup():
    help_text = "JesseJesse.com"
    popup = tk.Toplevel()
    popup.title("Help")
    popup.geometry("400x100")
    label = tk.Label(popup, text=help_text)
    label.pack(padx=10, pady=10)
    label.bind("<Button-1>", lambda e: webbrowser.open("https://JesseJesse.com"))

def open_github():
    webbrowser.open("https://github.com/sudo-self/video-snake/")

def update_footer():
    footer_label.config(text="Open")
    footer_label.config(bg='green')

def open_directory(event=None):
    directory = os.path.dirname(os.path.realpath(__file__))
    if platform.system() == 'Darwin':  # macOS
        subprocess.Popen(['open', directory])
    elif platform.system() == 'Linux':  # Linux
        subprocess.Popen(['xdg-open', directory])
    elif platform.system() == 'Windows':  # Windows
        subprocess.Popen(['explorer', directory])

root = tk.Tk()
root.title("VideoSnake by sudo-self")

label = tk.Label(root, text="source code", fg='white', cursor="hand2")
label.pack()
label.bind("<Button-1>", lambda e: open_github())

url_entry = tk.Entry(root, width=50, fg='gray')
url_entry.insert(0, "Enter the full URL https://")
url_entry.bind('<FocusIn>', on_focus_in)
url_entry.bind('<FocusOut>', on_focus_out)
url_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

install_button = tk.Button(button_frame, text="Install", command=install_youtube_dl)
install_button.pack(side=tk.LEFT)

quit_button = tk.Button(button_frame, text="Quit", command=quit_program)
quit_button.pack(side=tk.LEFT)

download_button = tk.Button(button_frame, text="Snake🐍", command=download_video)
download_button.pack(side=tk.LEFT)

paste_button = tk.Button(button_frame, text="Paste", command=paste_from_clipboard)
paste_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear", command=clear_url_entry)
clear_button.pack(side=tk.LEFT)

help_button = tk.Button(button_frame, text="Help", command=open_help_popup)
help_button.pack(side=tk.LEFT)


output_frame = tk.Frame(root)
output_frame.pack(fill=tk.BOTH, expand=True)

terminal_output = tk.Text(output_frame, wrap=tk.WORD, height=4)
terminal_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
terminal_output.config(state=tk.DISABLED)


footer_label = tk.Label(root, text="Made with Love", fg='white', cursor="hand2")
footer_label.pack()
footer_label.bind("<Button-1>", open_directory)

root.mainloop()





