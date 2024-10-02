import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube
from pytubefix.cli import on_progress


def install_packages(requirements_file='requirements.txt'):
    import subprocess
    import sys
    try:
        with open(requirements_file, 'r') as file:
            packages = file.readlines()

        for package in packages:
            package = package.strip()
            if package:
                print(f"Installing package: {package}")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        print("All packages installed successfully!")

    except FileNotFoundError:
        print(f"Error: {requirements_file} not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during installation: {e}")


def select_folder():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder = filedialog.askdirectory(initialdir=desktop_path)
    if folder:
        folder_label.config(text=folder)
    else:
        folder_label.config(text="")


def download_audio():
    url = url_entry.get()
    folder = folder_label.cget("text")

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    if folder == "":
        folder = os.path.join(os.path.expanduser("~"), "Desktop")

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Downloading: {yt.title}")
        ys = yt.streams.get_audio_only()
        ys.download(output_path=folder, filename=f"{yt.title}.mp3")
        messagebox.showinfo("Success", f"Download complete: {yt.title} saved to {folder}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # installs requirements.txt
    install_packages()

    # application
    root = tk.Tk()
    root.title("YouTube Audio Downloader")

    label = tk.Label(root, text="Enter YouTube URL:")
    label.pack(pady=10)

    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=10)

    folder_button = tk.Button(root, text="Select Folder", command=select_folder)
    folder_button.pack(pady=5)

    folder_label = tk.Label(root, text=f"{os.path.join(os.path.expanduser('~'), 'Desktop')}", wraplength=400,
                            justify="left")
    folder_label.pack(pady=10)

    download_button = tk.Button(root, text="Download", command=download_audio)
    download_button.pack(pady=20)

    root.mainloop()
