# Tech@JesseJesse.com
import tkinter as tk
import subprocess
import pyperclip
import os
import webbrowser

def download_video():
    url = url_entry.get()
    if url:
        subprocess.Popen(['youtube-dl', url])

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
#quit
def quit_program():
    os.kill(os.getpid(), 2)
#install tool
def install_youtube_dl():
    subprocess.Popen(['brew', 'install', 'youtube-dl'])
#help window
def open_help_popup():
    help_text = "github.com/sudo-self"
    popup = tk.Toplevel()
    popup.title("Help")
    popup.geometry("400x100")
    label = tk.Label(popup, text=help_text)
    label.pack(padx=10, pady=10)

def open_github():
    webbrowser.open("https://github.com/sudo-self/video-snake/")

root = tk.Tk()
root.title("VideoSnake by sudo-self")


label = tk.Label(root, text="github.com/sudo-self", fg='white', cursor="hand2")
label.pack()
label.bind("<Button-1>", lambda e: open_github())


url_entry = tk.Entry(root, width=50, fg='gray')
url_entry.insert(0, "Enter the full URL https://")
url_entry.bind('<FocusIn>', on_focus_in)
url_entry.bind('<FocusOut>', on_focus_out)
url_entry.pack()

#buttons
button_frame = tk.Frame(root)
button_frame.pack()


install_button = tk.Button(button_frame, text="Install", command=install_youtube_dl)
install_button.pack(side=tk.LEFT)


quit_button = tk.Button(button_frame, text="Quit", command=quit_program)
quit_button.pack(side=tk.LEFT)


download_button = tk.Button(button_frame, text="Snake", command=download_video)
download_button.pack(side=tk.LEFT)


paste_button = tk.Button(button_frame, text="Paste", command=paste_from_clipboard)
paste_button.pack(side=tk.LEFT)


clear_button = tk.Button(button_frame, text="Clear", command=clear_url_entry)
clear_button.pack(side=tk.LEFT)


help_button = tk.Button(button_frame, text="Help", command=open_help_popup)
help_button.pack(side=tk.LEFT)

root.mainloop()
