import tkinter as tk
from tkinter import ttk

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

# Updating button style for black text on #1ED760 background
style = ttk.Style()
style.configure("Accent.TButton", foreground="black", background="#1ED760", font=("Helvetica", 10))
style.map("Accent.TButton", background=[("active", "#1ED760")])

# Music Control Buttons
play_button = ttk.Button(control_frame, text="Play", width=10, style="Accent.TButton")
play_button.grid(row=0, column=0, padx=5)

pause_button = ttk.Button(control_frame, text="Pause", width=10, style="Accent.TButton")
pause_button.grid(row=0, column=1, padx=5)

skip_button = ttk.Button(control_frame, text="Skip", width=10, style="Accent.TButton")
skip_button.grid(row=0, column=2, padx=5)

# Exit Button with matching size
exit_button = ttk.Button(root, text="Exit", width=10, style="Accent.TButton", command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()