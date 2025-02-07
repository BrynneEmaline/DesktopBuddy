import tkinter as tk

class Window: # creating a window class
    def __init__(self): # constructor for each window instance
        self.root = tk.Tk()  # for each window instance, a root Tkinter window is created
        self.root.geometry("200x300") # sets window size
        self.root.overrideredirect(True) # removes title bar
        self.root.wm_attributes("-topmost", True) # keeps window on top
        self.root.wm_attributes("-transparentcolor", "white") # makes everything white transparent

    def get_root(self):
        return self.root