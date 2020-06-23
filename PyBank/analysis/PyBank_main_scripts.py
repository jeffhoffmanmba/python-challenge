# Create a Python script that analyzes the PyBank records to calculate each of the following:

import os
import csv

# initialize the directory
os.chdir(os.path.dirname(os.path.abspath(__file__))

# Set path for file
udemy_csv = os.path.join("..", "Resources", "budget_data.csv")

# Create Variables
months = []
net_total_profit_loss_amount = x

count_months = 0
net_total_profit_loss_amount = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0

# Open and read csv
with open(budget_data_csv_path newline="") as csvfile:

        csv_reader=csv.reader(csvfile, delimiter=",")

        #Read the header row first
        csv_header=next(csvfile)

# The total number of months included in the dataset
total_months_in_dataset = count_months +=1

# The net total amount of "Profit/Losses" over the entire period


# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# Print the analysis to the terminal and export a text file with the results

