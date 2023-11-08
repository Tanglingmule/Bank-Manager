import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

default_text = True
def delete_text(event):
  global default_text
  if default_text:
    username.delete(0, END)
    default_text = False


register_window = tk.Tk()
register_window.title('Register Now!')
register_window.attributes('-topmost', True)
register_window.geometry('600x600')
window_theme=ttk.Style(theme='cyborg')

username = ttk.Entry(register_window, style='info.Tentry')
username.pack(pady=50)
username.insert(END, 'Username Here')
username.bind("<Button-1>", delete_text)








register_window.mainloop()

