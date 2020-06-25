import os
import csv

# Set path for file
budget_data_csv_path = os.path.join('..', 'Resources', 'budget_data.csv')

# initialize the directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Create lists to store data
profit = []
monthly_changes = []
date = []

# Initialize starting variables at 0 to count 
count = 0
total_profit = 0
total_change_profit = 0
initial_profit = 0

# Open the CSV using the set path
with open(budget_data_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Conducting the ask
    for row in csvreader:    
      # Use count to count the number months in this dataset
      count = count + 1 

      # Will need it when collecting the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculate the average change in profits from month to month
      final_profit = int(row[1])
      monthly_change_profit = final_profit - initial_profit

      #Store these monthly changes in a list
      monthly_changes.append(monthly_change_profit)

      total_change_profit = total_change_profit + monthly_change_profit
      initial_profit = final_profit

      #Calculate the average change in profits
      average_change_profit = (total_change_profit/count)
      
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profit = max(monthly_changes)
      greatest_decrease_profit = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profit)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profit)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profit)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profit) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profit)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profit)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profit) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profit) + ")\n")
    text.write("----------------------------------------------------------\n")