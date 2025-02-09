
 ### **Modules for implementing Desktop Buddy**
- `Tkinter` : Graphical User Interface
  - create main window (root)
  - display buddy
  - handle user interactions
  - animations and movement
  - keeping the display window on top of other windows
  
 **Tkinter methods used:**
>   - **tk.Tk()** : creates a root window (returns a Tk instance), must be saved under a variable. </br>
> *note*: python doesn't use the 'new' keyword when creating instances of a class like in Java. 

>   - **geometry("widthxheight+x_offset+y_offset")** : defines the size and position of the window.
 
>   - **overrideredirect(True or False)** : Removes title bar, close button and window border. (True being a frameless window) </br>
> *note*: frameless windows can't be dragged normally, must add custom drag functionality.

>   - **config()** : configures widget properties. Parent class of all widgets (Label, Button, Frame, etc.), modifies widget properties. 
> Parameters vary depending on widget.

>   - **wm_attributes(attribute, value)** : modifies the appearance and behavior of the window. Common attributes include -fullscreen, -topmost, -transparentcolor, etc.

- `Pillow` : Python Imaging Library *(formerly PIL)* 
  - import and display images 
  - convert images into format Tkinter can interpret

- `os` : Operating Systems
  - allows for program to interact with different OS's
  - handles file paths and directories



**organizing project:**
 - main: entrypoint
 - window: handles the tkinter GUI
 - animations: logic for moving the buddy
 - config: stores global settings for screen size etc
 - assets: images and other assets for buddy
 - README: project documentation, is a markdown file

**python syntax as I learn it:** 

`__init__(self, param_2, param_3)` : python constructor, self must always be
the first parameter.

`self` : similar to java's 'this', but required even without redundant naming. 
All instance variables must use self. 

`root` : Tkinter naming convention for the main window. 

`def` : used to define a function.  
>example:   
>def say_hello():  
>>print("Hello!")

`import as ____` : assigning an alias to the imported module for brevity.




                
