import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import pandas as pd
import socket

database_userdata= pd.read_csv("database_login.csv")
print(database_userdata)

def check_details(username, password, recovery):
    #makes sure entries are populated
    if not recovery:
        if not username:
            Messagebox.show_error(message = 'No username', title = 'Invalid', parent = None, alert = True)
            return
        elif not password:
            Messagebox.show_error(message = 'No password', title = 'Invalid', parent= None, alert = True)
            return
        elif not database_userdata['Username'].str.contains(username).any():
            Messagebox.show_error(message= 'Username does not exist', title= 'Invalid', parent= None, alert= True)
            return
        else:  #compare password to the password stored for the username, it does this by creating a new data frame with all rows of matching usernames, then compares the first index of the password column to the users' inputted password
            row_correct = database_userdata[database_userdata['Username'] == username]
            if password != row_correct['Password'].values[0]:
                Messagebox.show_error(message= 'Incorrect Password', title= 'Invalid', parent= None, alert= True)
                return
    else:
        if recovery not in database_userdata:
            Messagebox.show_error(message= 'Recovery Key does not exist', title= 'Invalid', parent= None, alert= True)
    remember(var.get(), username)
    Messagebox.show_info(message= 'Logged In', alert= True, title= 'Logged In Successfully', parent= None)
    return True

def empty_entries(username_get, password_get, recovery_get):
    if username_get == username_placeholder:
        username.delete(0,'end')
    if password_get == password_placeholder:
        password.delete(0, 'end')
    if recovery_get == recovery_placeholder:
        recovery.delete(0, 'end')

def remember(state, username):
    if state:
        hostname = socket.gethostname() #get the hostname
        IP = socket.gethostbyname(hostname) #get ip from hostname

        # Find the row with the matching username and update the 'IP' column
        database_userdata.loc[database_userdata['Username'] == username, 'IP'] = IP

        # Save the updated DataFrame to the CSV file
        database_userdata.to_csv('database_login.csv', index=False)



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

login_window = tk.Tk()
login_window.title('Login Now!')
login_window.attributes('-topmost', True)
login_window.geometry('600x600')
window_theme=ttk.Style(theme='darkly')
var = tk.IntVar()

username_placeholder='Username here'
username = ttk.Entry(login_window, style='primary.Tentry')
username.pack(pady=5)
username.insert(END, username_placeholder)
username.bind('<FocusIn>',username_erase)
username.bind('<FocusOut>',username_add)


password_placeholder='Password here'
password = ttk.Entry(login_window, style='primary.Tentry')
password.pack(pady=5)
password.insert(END, password_placeholder)
password.bind('<FocusIn>', password_erase)
password.bind('<FocusOut>', password_add)

recovery_placeholder='Recovery Key here (OPTIONAL)'
recovery= ttk.Entry(login_window, style='primary.Tentry')
recovery.pack(pady=5)
recovery.insert(END, recovery_placeholder)
recovery.bind('<FocusIn>', recovery_erase)
recovery.bind('<FocusOut>', recovery_add)

login_button = ttk.Button(login_window, text='Click To Login', style='primary.Tbutton', command= lambda: [empty_entries(username.get(), password.get(), recovery.get()),check_details(username.get(),password.get(),recovery.get()),])
login_button.pack(pady=5)

remember_me = ttk.Checkbutton(login_window, text='Remember me', style='Roundtoggle.Toolbutton', variable= var)
remember_me.pack(pady=3)





login_window.mainloop()

