import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import pandas as pd
import random
import string

def generate_recovery():
    length=15
    characters = string.ascii_letters + string.digits
    
    generated_recovery=''.join(random.choice(characters) for i in range(length))
    return(generated_recovery)

def register_window():
    register= tk.Tk()
    register.title('Register Now!')
    register.attributes('-topmost', True)
    register.geometry('600x600')
    window_theme=ttk.Style(theme='darkly')

    email_placeholder='Email Here'
    email = ttk.Entry(register, style='primary.Tentry')
    email.pack(pady=5)
    email.insert(END, email_placeholder)
    email.bind('<FocusIn>',email_erase)
    email.bind('<FocusOut>',email_add)

    username_placeholder='Username here'
    username = ttk.Entry(register, style='primary.Tentry')
    username.pack(pady=5)
    username.insert(END, email_placeholder)
    username.bind('<FocusIn>',username_erase)
    username.bind('<FocusOut>',username_add)

    password_placeholder='Password Here'
    password = ttk.Entry(register, style='primary.Tentry')
    password.pack(pady=5)
    password.insert(END, email_placeholder)
    password.bind('<FocusIn>',password_erase)
    password.bind('<FocusOut>', password_add)
    
