import tkinter as tk
from database import create_db, add_income, add_expense, fetch_data
from gui import setup_gui
from dataanalysis import generate_report


root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("400x400")


add_income_button, add_expense_button, report_button = setup_gui(root)

add_income_button.config(command = add_income)
add_expense_button.config(command = add_expense)
report_button.config(command = generate_report)


root.mainloop()