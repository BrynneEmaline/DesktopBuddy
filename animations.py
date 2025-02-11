from PIL import Image, ImageTk
import os
import tkinter as tk
import random

class Animations:
    def __init__(self, root):
        self.root = root

        frame_folder_idle = "Assets/idle"
        self.idle_frames = [
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_idle, "mid.png" )).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_idle, "left.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_idle, "mid.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_idle, "right.png")).convert("RGBA")),
        ]
        self.idle_frame_index = 0

        frame_folder_walk_right = "Assets/walk_right"
        self.walk_right_frames = [
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_walk_right, "right1.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_walk_right, "right2.png")).convert("RGBA")),
        ]

        frame_folder_walk_left = "Assets/walk_left"
        self.walk_left_frames = [
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_walk_left, "left1.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_walk_left, "left2.png")).convert("RGBA")),
        ]

        frame_folder_happy = "Assets/happy"
        self.happy_frames = [
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_happy, "happy1.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_happy, "happy2.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_happy, "happy3.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_happy, "happy4.png")).convert("RGBA")),
        ]

        frame_folder_thinking = "Assets/thinking"
        self.thinking_frames = [
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_thinking, "thinking1.png")).convert("RGBA")),
            ImageTk.PhotoImage(Image.open(os.path.join(frame_folder_thinking, "thinking2.png")).convert("RGBA")),
        ]

        self.idle_frame_index = 0
        self.happy_frame_index = 0
        self.thinking_frame_index = 0
        self.current_walk_frames = None
        self.walk_frame_index = 0

        self.bob = tk.Label(root, bg="white")
        self.bob.place(x=100, y=150)

        self.mode = "idle"

        self.bob.bind("<ButtonPress-1>", self.start_drag)
        self.bob.bind("<B1-Motion>", self.drag)

        self.animate_idle()
        self.schedule_special_idle()
        self.schedule_walk()

    def start_drag(self, event):
        self.offset_x = event.x_root - self.root.winfo_x()
        self.offset_y = event.y_root - self.root.winfo_y()

    def drag(self, event):
        new_x = event.x_root - self.offset_x
        new_y = event.y_root - self.offset_y
        self.root.geometry(f"+{new_x}+{new_y}")

    def animate_idle(self):
        if self.mode == "idle":
            self.bob.config(image=self.idle_frames[self.idle_frame_index])
            self.idle_frame_index = (self.idle_frame_index + 1) % len(self.idle_frames)
            self.root.after(500, self.animate_idle)

    def start_happy(self):
        self.mode = "happy"
        self.happy_frame_index = 0
        self.animate_happy()
        self.root.after(5000, self.end_special_idle)

    def animate_happy(self):
        if self.mode == "happy":
            self.bob.config(image=self.happy_frames[self.happy_frame_index])
            self.happy_frame_index = (self.happy_frame_index + 1) % len(self.happy_frames)
            self.root.after(200, self.animate_happy)

    def start_thinking(self):
        self.mode = "thinking"
        self.thinking_frame_index = 0
        self.animate_thinking()
        self.root.after(5000, self.end_special_idle)

    def animate_thinking(self):
        if self.mode == "thinking":
            self.bob.config(image=self.thinking_frames[self.thinking_frame_index])
            self.thinking_frame_index = (self.thinking_frame_index + 1) % len(self.thinking_frames)
            self.root.after(400, self.animate_thinking)

    def end_special_idle(self):
        self.mode = "idle"
        self.idle_frame_index = 0
        self.animate_idle()
        self.schedule_special_idle()

    def schedule_special_idle(self):
        delay = random.randint(5000, 15000)
        choice = random.choice(["happy", "thinking"])
        if choice == "happy":
            self.root.after(delay, self.start_happy)
        else:
            self.root.after(delay, self.start_thinking)

    def animate_walk(self):
        if self.mode == "walking":
            self.bob.config(image=self.current_walk_frames[self.walk_frame_index])
            self.walk_frame_index = (self.walk_frame_index + 1) % len(self.current_walk_frames)
            self.root.after(500, self.animate_walk)

    def schedule_walk(self):
        delay = random.randint(5000, 10000)
        self.root.after(delay, self.start_walk)

    def start_walk(self):
        self.mode = "walking"
        self.walk_frame_index = 0

        info = self.bob.place_info()
        self.start_x = int(info.get("x", 0))
        self.start_y = int(info.get("y", 0))

        move_distance = random.randint(-100, 100)
        self.target_x = self.start_x + move_distance
        self.target_y = self.start_y

        if move_distance < 0:
            self.current_walk_frames = self.walk_left_frames
        else:
            self.current_walk_frames = self.walk_right_frames

        self.animate_walk()

        self.walk_steps = 20
        self.current_step = 0
        self.move_walk_step()

    def move_walk_step(self):
        if self.current_step < self.walk_steps:
            new_x = self.start_x + (self.target_x - self.start_x) * (self.current_step / self.walk_steps)
            new_y = self.start_y + (self.target_y - self.start_y) * (self.current_step / self.walk_steps)
            self.bob.place_configure(x=int(new_x), y=int(new_y))
            self.current_step += 1
            self.root.after(100, self.move_walk_step)
        else:
            self.mode = "idle"
            self.idle_frame_index = 0
            self.animate_idle()
            self.schedule_walk()
