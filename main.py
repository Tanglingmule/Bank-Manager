import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import pandas as pd
import socket
import registerpage as register
import loginpage as login

def main_page():
    main_window = tk.Tk()
    main_window.title('Doyoda')
    main_window.attributes('-topmost', True)
    main_window.geometry('600x600')
    window_theme=ttk.Style(theme='darkly')
    var = tk.IntVar()


    