# First import the os module
import os

# Module for reading CSV files
import csv

#Define the Variables
months = []
net_total_profit_loss_amount = []

count_months = 0
net_total_profit_loss_amount = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# initialize the directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Set path for file
budget_data_csv_path = os.path.join('..', 'Resources', 'budget_data.csv')

# CSV reader specifies delimiter and variable that holds contents
with open(budget_data_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #Prints CSV file header in terminal
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csv_reader:

    # The total number of months included in the dataset
        count_months +=1

    print(f"Total Months: {count_months}")