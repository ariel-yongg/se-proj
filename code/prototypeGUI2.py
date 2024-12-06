import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initializing main window
root = tk.Tk()
root.title("Facial Harmony (Prototype GUI)")
root.geometry("400x350")
root.configure(bg="black")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Facial Harmony", font=("Helvetica", 16, "bold"), fg="white", bg="black")
title_label.pack(pady=10)

# Emotion Display Frame
emotion_frame = tk.Frame(root, bd=2, relief="sunken", bg="black")
emotion_frame.pack(pady=10, padx=20, fill="x")

emotion_label_title = tk.Label(emotion_frame, text="Detected Emotion:", font=("Helvetica", 12), fg="white", bg="black")
emotion_label_title.pack(anchor="w", padx=10)

emotion_label = tk.Label(emotion_frame, text="Neutral", font=("Helvetica", 12, "italic"), fg="#1DB954", bg="black")
emotion_label.pack(anchor="w", padx=20)

# Song Display Frame
song_frame = tk.Frame(root, bd=2, relief="sunken", bg="black")
song_frame.pack(pady=10, padx=20, fill="x")

song_label_title = tk.Label(song_frame, text="Now Playing:", font=("Helvetica", 12), fg="white", bg="black")
song_label_title.pack(anchor="w", padx=10)

song_label = tk.Label(song_frame, text="No Song Selected", font=("Helvetica", 12, "italic"), fg="#1DB954", bg="black")
song_label.pack(anchor="w", padx=20)

# Music Controls Frame
control_frame = tk.Frame(root, bg="black")
control_frame.pack(pady=20)

# Load button images
def load_image(file_path, size):
    img = Image.open(file_path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

rewind_icon = load_image("rewind_icon.png", (30, 30))
play_icon = load_image("play_icon.png", (30, 30))
pause_icon = load_image("pause_icon.png", (30, 30))
skip_icon = load_image("skip_icon.png", (30, 30))

# Define button style
style = ttk.Style()
style.theme_use("default")
style.configure("Music.TButton",
                background="black",
                borderwidth=2,
                relief="raised",
                bordercolor="#1DB954",
                highlightcolor="#1DB954",
                padding=2)
style.map("Music.TButton",
          background=[("active", "black")],
          bordercolor=[("active", "#1DB954")])

# Add style for the Exit button with green text
style.configure("Exit.TButton",
                foreground="#1DB954",
                background="white",
                borderwidth=2,
                relief="raised",
                bordercolor="#1DB954",
                highlightcolor="#1DB954",
                padding=2)

# Function to toggle play/pause
is_playing = tk.BooleanVar(value=True)  # Tracks if the button is in "playing" state


def toggle_play_pause():
    if is_playing.get():
        play_pause_button.config(image=play_icon)
        is_playing.set(False)
    else:
        play_pause_button.config(image=pause_icon)
        is_playing.set(True)


# Music Control Buttons
rewind_button = ttk.Button(control_frame, image=rewind_icon, style="Music.TButton")
rewind_button.grid(row=0, column=0, padx=5)

play_pause_button = ttk.Button(control_frame, image=pause_icon, style="Music.TButton", command=toggle_play_pause)
play_pause_button.grid(row=0, column=1, padx=5)

skip_button = ttk.Button(control_frame, image=skip_icon, style="Music.TButton")
skip_button.grid(row=0, column=2, padx=5)

# Exit Button
exit_button = ttk.Button(root, text="Exit", width=10, style="Exit.TButton", command=root.destroy)
exit_button.pack(pady=10)

# Keep references to images to avoid garbage collection
root.rewind_icon = rewind_icon
root.play_icon = play_icon
root.pause_icon = pause_icon
root.skip_icon = skip_icon

root.mainloop()