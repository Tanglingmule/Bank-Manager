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

    def update_details(username):

            new_details_window = tk.Toplevel()
            new_details_window.title('New Bank Details')
            new_details_window.attributes('-topmost', True)
            new_details_window.geometry('300x300')

            
            def details_erase(event=None):
                if details.get() == details_placeholder:
                    details.delete(0,'end')
            def details_add(event=None):
                if details.get() == '':
                    details.insert(0,details_placeholder)
            
            def empty_entries(details_get):
                if details_get == details_placeholder:
                    details.delete(0,'end')

            def repopulate_entries(details_get):
                if details_get == '':
                    username.insert(0, details_placeholder)

            def check_filled(details):
                if not details:
                    Messagebox.show_error(message= 'No Details entered', title= 'Invalid', parent= None, alert= True)
                    return False
                else:
                    return True
            
            def check_existing(details_get):    #checks the database for accounts with the same username or email
                if database_bankdata['BankDetails'].astype(str).str.contains(str(details_get)).any():
                    Messagebox.show_error(message= 'Details already exists', title= 'Invalid', parent= None, alert= True)
                    return False
                else:
                    return True
            
            def all_verify(details):
                filled = check_filled(details)
                if filled == True:
                        exist = check_existing(details)
                        if exist == True: 
                # if all are true, add file 
                            add_file(details)

            def add_file(details):
                #ADDING DETAILS TO THE BANK DETAILS FILE
                # Find the row with the matching username and update the 'IP' column
                database_bankdata.loc[database_bankdata['Username'] == username, 'BankDetails'] = details

                # Save the updated DataFrame to the CSV file
                database_bankdata.to_csv('database_banking.csv', index=False)

            
            details_placeholder='Details Here'
            details = ttk.Entry(new_details_window, style='primary.Tentry')
            details.pack(pady=5)
            details.insert(END, details_placeholder)
            details.bind('<FocusIn>',details_erase)
            details.bind('<FocusOut>',details_add)


            new_details_button = ttk.Button(new_details_window, text='Click To Update Details', style='primary.Tbutton', command= lambda: [empty_entries(details.get()),all_verify(details.get()), repopulate_entries(details.get())])
            new_details_button.pack(pady=5)
        

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

        details_label = ttk.Label(details_window, text = 'Your card number is: '+ details)
        details_label.pack(pady = 20)

        button_update_details = ttk.Button(details_window, text='Update Your Bank Details', command= lambda: update_details(username))
        button_update_details.pack(pady=10)

        details_window.mainloop()