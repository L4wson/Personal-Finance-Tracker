import pandas as pd
import matplotlib.pyplot as plt
from database import fetch_data
def fetch_data_from_db():
    income_data = fetch_data('income')
    expenses_data = fetch_data('expenses')
    return income_data, expenses_data

def process_data(income_data, expenses_data):
    income_df  = pd.DataFrame(income_data, columns = ['amount', 'source', 'date', 'description']) 
    expenses_df = pd.DataFrame(expenses_data, columns = ['amount', 'source', 'date', 'description'])

def generate_report():
    income_data = fetch_data('income')
    expenses_data = fetch_data("expenses")
    process_data(income_data, expenses_data)
    plt.bar(...)
    plt.show()

def display_visualizations():
    plt.savefig('report.png')
    plt.show()
