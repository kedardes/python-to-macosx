import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk
root = tk.Tk()
root.title("Yum")
tk.Button(root, text="Express Pizza Delivery").pack()
tk.mainloop()