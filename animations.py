from PIL import Image, ImageTk
import os
import tkinter as tk

class Animations:
    def __init__(self, root):
        self.root = root

        frame_folder = "Assets/idle"
        self.frames = [
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder, "mid.png" )).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder, "left.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder, "mid.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder, "right.png")).convert("RGBA")),
        ]

        self.frame_index = 0

        self.bob = tk.Label(root, bg="white")
        self.bob.pack(side="right")

        self.animate()

    def animate(self):
        self.bob.config(image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.root.after(150, self.animate)














# what i think is next: import frames, create a loop wherein it goes from frame
# to frame