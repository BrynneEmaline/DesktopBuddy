from window import Window
from animations import Animations

app = Window()
root = app.get_root()
animation = Animations(root)

root.mainloop() # keeps window open