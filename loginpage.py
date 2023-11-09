import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import pandas as pd

def check_details(username, password, recovery):
    #make sure entries are populated
    if not recovery:
        if not username:
            Messagebox.show_error(message = 'No username', title = 'Invalid', parent = None, alert = True)
            pass
        elif not password:
            Messagebox.show_error(message = 'No password', title = 'Invalid', parent= None, alert = True)
            pass
        elif username != #username from database:
            Messagebox.show_error(message= 'Username does not exist', title= 'Invalid', parent= None, alert= True)
            pass
        else:
            #compare password to the password stored for the username
    else:
        if recovery != #recovery from database:
            Messagebox.show_error(message= 'Recovery Key does not exist', title= 'Invalid', parent= None, alert= True)
    Messagebox.ok(message= 'Logged In', alert= True, title= 'Logged In Successfully', parent= None)
    return True

def empty_entries(username_get, password_get, recovery_get):
    if username_get == username_placeholder:
        username.delete(0,'end')
    if password_get == password_placeholder:
        password.delete(0, 'end')
    if recovery_get == recovery_placeholder:
        recovery.delete(0, 'end')


def username_erase(event=None):
    if username.get() == username_placeholder:
        username.delete(0,'end')
def username_add(event=None):
    if username.get() == '':
        username.insert(0,username_placeholder)

def password_erase(event=None):
    if password.get() == password_placeholder:
        password.delete(0,'end')
def password_add(event=None):
    if password.get() == '':
        password.insert(0,password_placeholder)

def recovery_erase(event=None):
    if recovery.get() == recovery_placeholder:
        recovery.delete(0,'end')
def recovery_add(event=None):
    if recovery.get() == '':
        recovery.insert(0,recovery_placeholder)

register_window = tk.Tk()
register_window.title('Login Now!')
register_window.attributes('-topmost', True)
register_window.geometry('600x600')
window_theme=ttk.Style(theme='darkly')

username_placeholder='Username here'
username = ttk.Entry(register_window, style='info.Tentry')
username.pack(pady=5)
username.insert(END, username_placeholder)
username.bind('<FocusIn>',username_erase)
username.bind('<FocusOut>',username_add)


password_placeholder='Password here'
password = ttk.Entry(register_window, style='info.Tentry')
password.pack(pady=5)
password.insert(END, password_placeholder)
password.bind('<FocusIn>', password_erase)
password.bind('<FocusOut>', password_add)

recovery_placeholder='Recovery Key here (OPTIONAL)'
recovery= ttk.Entry(register_window, style='info.Tentry')
recovery.pack(pady=5)
recovery.insert(END, recovery_placeholder)
recovery.bind('<FocusIn>', recovery_erase)
recovery.bind('<FocusOut>', recovery_add)

login_button = ttk.Button(register_window, text='Click To Login', style='info.Tbutton', command= lambda: [empty_entries(username.get(), password.get(), recovery.get()),check_details(username.get(),password.get(),recovery.get()),])
login_button.pack(pady=5)






register_window.mainloop()

