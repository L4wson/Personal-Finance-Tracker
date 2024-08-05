import tkinter as tk

def setup_gui(root):
    add_income_button = tk.Button( text= "Add Income")
    add_income_button.pack()

    add_expense_button = tk.Button( text= "Add Expense")
    add_expense_button.pack()

    report_button = tk.Button(text = "Generate Report")
    report_button.pack()
    
    return add_expense_button, add_income_button, report_button