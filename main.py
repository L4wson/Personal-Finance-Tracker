import tkinter as tk
from tkinter import ttk
import darkdetect
import sv_ttk
import pywinstyles
from database import create_db, add_income, add_expense, fetch_data
from gui import setup_gui
from dataanalysis import generate_report

create_db()

root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("400x400")


add_income_button, add_expense_button, report_button = setup_gui(root)

add_income_button.config(command =lambda: add_income('amount', 'source', 'date', 'description'))
add_expense_button.config(command =lambda: add_expense('amount', 'category', 'date', 'description'))
report_button.config(command = generate_report)

pywinstyles.apply_style(root, 'optimised')
sv_ttk.set_theme("dark")
root.mainloop()