import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import pandas as pd
import socket
import registerpage as register

database_bankdata = pd.read_csv('database_banking.csv')

def main_page(username):
    main_window = tk.Toplevel()
    main_window.title('Halifax')
    main_window.attributes('-topmost', True)
    main_window.geometry('600x600')
    window_theme=ttk.Style(theme='darkly')
    var = tk.IntVar()


    welcome = ttk.Label(main_window,text='Welcome '+username)
    welcome.pack(pady=5)

    bank_details = ttk.Button(main_window, text='Bank Details', command = lambda:details_page(username))
    bank_details.pack(pady=5)

    bank_balance = ttk.Button(main_window, text='Balance', command= lambda:balance_page(username))
    bank_balance.pack(pady=5)

    bank_transaction = ttk.Button(main_window, text='Transaction')
    bank_transaction.pack(pady=5)

    bank_history = ttk.Button(main_window, text= 'Transaction History')
    bank_history.pack(pady=5)


def balance_page(username):

    balance_window = tk.Toplevel()
    balance_window.title('Balance Page')
    balance_window.attributes('-topmost', True)
    balance_window.geometry('300x300')

    row_correct = database_bankdata.loc[database_bankdata['Username'] == username]
    balance = row_correct['BankBalance'].values[0]

    # Create a StringVar to update the label dynamically
    balance_var = tk.StringVar(value=f'Your Balance is: {balance}')

    # Create a ttk.Label to display the balance
    balance_label = ttk.Label(balance_window, textvariable=balance_var)
    balance_label.pack(pady=10)
   
    balance_window.mainloop()

def details_page(username):
    details_window = tk.Toplevel()
    details_window.title('Bank Details')
    details_window.attributes('-topmost', True)
    details_window.geometry('300x300')

    row_correct = database_bankdata.loc[database_bankdata['Username'] == username]
    details = row_correct['BankDetails'].values[0]

    #create a label to display
    details = str(details)

    if details =='nan':
        details='No Details Have Been Given'

    details_label = ttk.Label(details_window, text = details)
    details_label.pack(pady = 20)

    update_details = ttk.Button(details_window, text='Update Your Bank Details')
    update_details.pack(pady=10)

    details_window.mainloop()
