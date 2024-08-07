import tkinter as tk
from tkinter import ttk

def setup_gui(root):
    add_income_button = ttk.Button( text= "Add Income")
    add_income_button.pack()

    add_expense_button = ttk.Button( text= "Add Expense")
    add_expense_button.pack()

    report_button = ttk.Button(text = "Generate Report")
    report_button.pack()
    
    return add_expense_button, add_income_button, report_button