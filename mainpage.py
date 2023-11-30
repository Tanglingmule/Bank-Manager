import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import pandas as pd
import socket
import registerpage as register


def main_page(username):
    main_window = tk.Toplevel()
    main_window.title('Halifax')
    main_window.attributes('-topmost', True)
    main_window.geometry('600x600')
    window_theme=ttk.Style(theme='darkly')
    var = tk.IntVar()


    welcome = ttk.Label(main_window,text='Welcome '+username)
    welcome.pack(pady=5)

    bank_details = ttk.Button(main_window, text='Bank Details')
    bank_details.pack(pady=5)

    bank_balance = ttk.Button(main_window, text='Balance')
    bank_balance.pack(pady=5)

    bank_transaction = ttk.Button(main_window, text='Transaction')
    bank_transaction.pack(pady=5)

    bank_history = ttk.Button(main_window, text= 'Transaction History')
    bank_history.pack(pady=5)


def balance_page(username):
    database_bankdata.loc[database_bankdata['Username'] == username]
    