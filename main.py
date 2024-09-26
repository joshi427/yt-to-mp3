import tkinter as tk
from tkinter import messagebox
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_audio():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Downloading: {yt.title}")

        ys = yt.streams.get_audio_only()
        ys.download(mp3=True)

        messagebox.showinfo("Success", f"Download complete: {yt.title}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("YouTube Audio Downloader")

label = tk.Label(root, text="Enter YouTube URL:")
label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

download_button = tk.Button(root, text="Download", command=download_audio)
download_button.pack(pady=20)

root.mainloop()

