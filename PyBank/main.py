import os
import csv

# Variables
total_months = 0
net_total = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set Path & open file
csvpath = r'Resources\budget_data.csv'
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read The Header Row
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Set Variables For Rows
    previous_row = int(row[1])
    total_months = total_months + 1
    net_total = net_total + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Task Begins
    for row in csvreader:
        
        # The total number of months included in the dataset
        total_months = total_months + 1
        
        # The net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(row[1])

        # Calculate the changes
        
        Profit_change = int(row[1]) - previous_row
        monthly_change.append(Profit_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # The average of the changes in "Profit/Losses" over the entire period / Min&Max of the Changes
    average_change = sum(monthly_change)/ len(monthly_change)
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print
print(f"Financial Analysis")
print(f"--------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: $({average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")


# Output
result = r'analysis\PyBank_Result.text'
print(result)

with open(result, 'w',) as txtfile:

    # txtfile Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
