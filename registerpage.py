import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import pandas as pd
import random
import string
from emailsuffixes import all_email_suffixes

database_userdata= pd.read_csv("database_login.csv")


def generate_recovery():
    length=15
    characters = string.ascii_letters + string.digits
    
    generated_recovery=''.join(random.choice(characters) for i in range(length))
    Messagebox.show_info(message= 'Your Recovery Key is: ' + generated_recovery, title= 'Recovery Key Generated', parent= None, alert= True)
    return(generated_recovery)

def check_existing(username_get, email_get):    #checks the database for accounts with the same username or email
    if database_userdata['Username'].str.contains(username_get).any():
        Messagebox.show_error(message= 'Username already exists', title= 'Invalid', parent= None, alert= True)
    if database_userdata['Email'].str.contains(email_get).any():
        Messagebox.show_error(message= 'Email is already in use for another active account', title= 'Invalid', parent= None, alert= True)

def check_filled(username, password, email):
    if not username:
        Messagebox.show_error(message= 'No username entered', title= 'Invalid', parent= None, alert= True)
    if not password:
        Messagebox.show_error(message= 'No password entered', title= 'Invalid', parent= None, alert= True)
    if not email:
         Messagebox.show_error(message= 'No email entered', title= 'Invalid', parent= None, alert= True)

def email_verify(email):
    split_email= email.split('@')
    if split_email[1] not in all_email_suffixes:
        Messagebox.show_error(message= 'This is not a valid email provider', title= 'Invalid', parent= None, alert= True)




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
    
    def add_file(username, password, email, recovery):
        IP='NaN'
        new_row = pd.DataFrame([[username, password, email, recovery, IP]], columns=['Username', 'Password', 'Email', 'Recoverykey','IP'])
        new_database_userdata = pd.concat([database_userdata, new_row], ignore_index=True)
        new_database_userdata.to_csv('database_login.csv', index= False)

    


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

    register_button = ttk.Button(register, text='Click To Register', style='primary.Tbutton', command= lambda: [empty_entries(username.get(), password.get(), email.get()),all_verify(username.get(), password.get(), email.get())])
    register_button.pack(pady=5)

     #need to verify all at once on button press 
    def all_verify(username, password, email):
        check_filled(username, password, email)
        if check_filled() == True:
            email_verify(email)
            if email_verify() == True:
                check_existing(username, email)

        # if all are true, add file 
        add_file(username, password, email)

    
    register.mainloop()
    
