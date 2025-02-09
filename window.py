import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x300")
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.config(bg="white")
        self.root.wm_attributes("-transparentcolor", "white")

    def get_root(self):
        return self.root
