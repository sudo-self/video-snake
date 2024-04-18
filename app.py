from flask import Flask, render_template, request, jsonify
import subprocess
import pyperclip
import os
import webbrowser

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    if url:
        subprocess.Popen(['youtube-dl', url])
    return '', 204

@app.route('/paste', methods=['POST'])
def paste_from_clipboard():
    clipboard_text = pyperclip.paste()
    return jsonify({'text': clipboard_text})

@app.route('/quit', methods=['POST'])
def quit_program():
    os.kill(os.getpid(), 2)
    return '', 204

@app.route('/install', methods=['POST'])
def install_youtube_dl():
    subprocess.Popen(['sudo', '-u', 'nonrootuser', 'brew', 'install', 'youtube-dl'])
    return '', 204

@app.route('/help')
def open_help_popup():
    help_text = "github.com/sudo-self"
    return help_text

@app.route('/github')
def open_github():
    webbrowser.open("https://github.com/sudo-self/video-snake/")
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
