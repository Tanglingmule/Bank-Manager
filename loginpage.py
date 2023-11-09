import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import pandas as pd

def check_details(username, password, recovery):
  if not recovery:
    if not username:
      Messagebox.show_error(message='No username', title='Invalid', parent=None, alert=True)


default_text = True
def delete_text_username(event):
  global default_text
  if default_text:
    username.delete(0, END)
    default_text = False
    default_text = True

def delete_text_password(event):
  global default_text
  if default_text:
    password.delete(0, END)
    default_text = False
    default_text = True

def delete_text_recovery(event):
  global default_text
  if default_text:
    recovery.delete(0, END)
    default_text = False
    default_text = True

register_window = tk.Tk()
register_window.title('Login Now!')
register_window.attributes('-topmost', True)
register_window.geometry('600x600')
window_theme=ttk.Style(theme='darkly')

username_placeholder='Username here'
username = ttk.Entry(register_window, style='info.Tentry')
username.pack(pady=5)
username.insert(END, username_placeholder)
username.bind("<Button-1>", delete_text_username)

password_placeholder='Password here'
password = ttk.Entry(register_window, style='info.Tentry')
password.pack(pady=5)
password.insert(END, password_placeholder)
password.bind('<Button-1>', delete_text_password)

recovery_placeholder='Recovery Key here (OPTIONAL)'
recovery= ttk.Entry(register_window, style='info.Tentry')
recovery.pack(pady=5)
recovery.insert(END, recovery_placeholder)
recovery.bind('<Button-1>', delete_text_recovery)

login_button = ttk.Button(register_window, text='Click To Login', style='info.Tbutton', command=check_details('','',''))
login_button.pack(pady=5)






register_window.mainloop()

