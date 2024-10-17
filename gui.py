import tkinter as tk
from tkinter import ttk

def setup_gui(root):

    amount_label = ttk.Label(text = "Amount")
    amount_label.grid(row = 0, column = 0)
    amount_entry = ttk.Entry()
    amount_entry.grid(row = 0, column = 1)
    
    add_income_button = ttk.Button(text= "Add Income")
    add_income_button.grid(row = 4, column = 0)
    add_income_button.grid()

    add_expense_button = ttk.Button(text= "Add Expense")
    add_expense_button.grid()

    report_button = ttk.Button(text = "Generate Report")
    report_button.grid()
    
    return add_expense_button, add_income_button, report_button