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

    register= tk.Toplevel()
    register.title('Register Now!')
    register.attributes('-topmost', True)
    register.geometry('600x600')
    

    def username_erase(event=None):
        if username.get() == username_placeholder:
            username.delete(0,'end')
    def username_add(event=None):
        if username.get() == '':
            username.insert(0,username_placeholder)
        
    def email_erase(event=None):
        if email.get() == email_placeholder:
            email.delete(0, END)
    def email_add(event=None):
        if email.get() == email_placeholder:
            email.delete(0, END)
    def password_erase(event=None):
        if password.get() == password_placeholder:
            password.delete(0, END)
    def password_add(event=None):
        if password.get() == '':
            password.insert(0,password_placeholder)

    def empty_entries(username_get, password_get, email_get):
        if username_get == username_placeholder:
            username.delete(0,'end')
        if password_get == password_placeholder:
            password.delete(0, 'end')
        if email_get == email_placeholder:
            email.delete(0, 'end')
            

    email_placeholder='Email Here'
    email = ttk.Entry(register, style='primary.Tentry')
    email.pack(pady=5)
    email.insert(END, email_placeholder)
    email.bind('<FocusIn>',email_erase)
    email.bind('<FocusOut>',email_add)

    username_placeholder='Username here'
    username = ttk.Entry(register, style='primary.Tentry')
    username.pack(pady=5)
    username.insert(END, username_placeholder)
    username.bind('<FocusIn>',username_erase)
    username.bind('<FocusOut>',username_add)

    password_placeholder='Password Here'
    password = ttk.Entry(register, style='primary.Tentry')
    password.pack(pady=5)
    password.insert(END, password_placeholder)
    password.bind('<FocusIn>',password_erase)
    password.bind('<FocusOut>', password_add)

    register_button = ttk.Button(register_window, text='Click To Register', style='primary.Tbutton', command= lambda: [empty_entries(username.get(), password.get(), email.get()),check_details(username.get(),password.get(),email.get()),])
    register_button.pack(pady=5)

    register.mainloop()
    
