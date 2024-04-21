#Python tk Author: Jesse@JesseJesse.com
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import subprocess
import pyperclip
import os
import webbrowser
import platform
import threading

def download_video():
    url = url_entry.get()
    if url:
        threading.Thread(target=download_video_thread, args=(url,), daemon=True).start()

def download_video_thread(url):
    process = subprocess.Popen(['yt-dlp', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = process.communicate()
    update_terminal(out, err)
    update_footer()

def update_terminal(out, err):
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END)
    terminal_output.insert(tk.END, out)
    terminal_output.insert(tk.END, err)
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
    if url_entry.get() == "Enter the full URL and press the snake button":
        url_entry.delete(0, tk.END)
        url_entry.config(fg='white')

def on_focus_out(event):
    if not url_entry.get():
        url_entry.insert(0, "Enter the full URL and press the snake button")
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

def update_footer():
    footer_label.config(text="Open")
    footer_label.config(bg='green')

def open_directory(event=None):
    directory = os.path.dirname(os.path.realpath(__file__))
    if platform.system() == 'Darwin':  
        subprocess.Popen(['open', directory])
    elif platform.system() == 'Linux': 
        subprocess.Popen(['xdg-open', directory])
    elif platform.system() == 'Windows': 
        subprocess.Popen(['explorer', directory])

def update_gif(frame_number=0):
    global frames, gif_label, root
    gif_label.config(image=frames[frame_number])
    frame_number = (frame_number + 1) % len(frames)
    root.after(100, update_gif, frame_number)

root = tk.Tk()
root.title("Snake Video Anywhere")

url_entry = tk.Entry(root, width=50, fg='gray', bd=2, relief=tk.SOLID)
url_entry.insert(0, "enter the full URL and press the snake button")
url_entry.bind('<FocusIn>', on_focus_in)
url_entry.bind('<FocusOut>', on_focus_out)
url_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

install_button = tk.Button(button_frame, text="Install", command=install_youtube_dl, bd=2, relief=tk.SOLID, bg='blue', fg='black')
install_button.pack(side=tk.LEFT)

quit_button = tk.Button(button_frame, text="Quit", command=quit_program, bd=2, relief=tk.SOLID, bg='blue', fg='black')
quit_button.pack(side=tk.LEFT)

download_button = tk.Button(button_frame, text="🐍", command=download_video, bd=2, relief=tk.SOLID, bg='blue', fg='black')
download_button.pack(side=tk.LEFT)

paste_button = tk.Button(button_frame, text="Paste", command=paste_from_clipboard, bd=2, relief=tk.SOLID, bg='blue', fg='black')
paste_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear", command=clear_url_entry, bd=2, relief=tk.SOLID, bg='blue', fg='black')
clear_button.pack(side=tk.LEFT)

help_button = tk.Button(button_frame, text="Help", command=open_help_popup, bd=2, relief=tk.SOLID, bg='blue', fg='black')
help_button.pack(side=tk.LEFT)


output_frame = tk.Frame(root)
output_frame.pack(fill=tk.BOTH, expand=True)


gif_path = "giphy.gif"
gif_image = Image.open(gif_path)
frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(gif_image)]


gif_label = tk.Label(output_frame)
gif_label.pack()


update_gif()

terminal_output = tk.Text(output_frame, wrap=tk.WORD, height=4)
terminal_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
terminal_output.config(state=tk.DISABLED)

footer_label = tk.Label(root, text="python3 vsnake.py", fg='white', cursor="hand2")
footer_label.pack()
footer_label.bind("<Button-1>", open_directory)

root.mainloop()












