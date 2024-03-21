
"""
Aaron PenKruger
"python-challenge 'PyBank'" Due 3/21/2024

This assigment, 'python-challenge', was to find the following values from a csv file, 'budget_data.csv':


The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period

The dataset is composed of two columns: "Date" and "Profit/Losses"
"""


# Import Modules
import os
import csv


# Path to collect "Budget_data.csv from folder"
budget_data_path = os.path.join("..","Resources","budget_data.csv")

with open(budget_data_path,"r") as csvfile:
    
    # Split the data at the commas
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip Header
    header = next(csvreader)
    

    # Set initial values for variables "Total Months", "Net Profit/Losses", "Greatest Profit", "Greatest Loss"
    # Create list of changes in proffit/losses to be appended per month

    total_months = 0
    net_prof = 0
    greatest_prof_increase = 0 
    greatest_prof_decrease = 0
    prof_amounts = []
    prof_change_list = []
    greatest_loss_month = "None"
    greatest_prof_month = "None"
    previous_month_profit= None


    #Begin for-loop Iteration of rows to find & Calculate Values
    for row in csvreader:
       
        #Initialize Variables for iteration
        this_month_profit = int(row[1])
        this_month = str(row[0])

        # Sum the total months
        total_months += 1

        # Sum the net profit
        net_prof += this_month_profit


        
        # Find Monthly Profit Change
        if previous_month_profit is not None:

            profit_change = this_month_profit - previous_month_profit


            #Create list of Profit changes
            prof_change_list.append(profit_change)
            

            # Check greatest profit increase and hold in variable
            if greatest_prof_increase < profit_change:
                greatest_prof_increase = profit_change
                greatest_prof_month = this_month

            # Check for greatest profit decrease and hold in variable
            if greatest_prof_decrease > profit_change:
                greatest_prof_decrease = profit_change
                greatest_loss_month = this_month
        
        #Reset Variable for next iteration
        previous_month_profit = this_month_profit

        # Restart row iteration

    #Calculate Average Profit Increase/Decrease rounded to two decimal points 
    average_profit_change = round(sum(prof_change_list)/len(prof_change_list), 2)



# Store Results
analysis_results = \
f"""\nFinancial Analysis

------------------

Total Months: {total_months}
Total: ${net_prof}
Average Change: ${average_profit_change}
Greatest Increase in Profits: {greatest_prof_month} $({greatest_prof_increase})
Greatest Decrease in Profits: {greatest_loss_month} $({greatest_prof_decrease})

"""

 # Print Results
print(analysis_results)

# export text file
output_file_path = "financial_analysis.txt"

with open(output_file_path, "w") as output_file: 
    output_file.write(analysis_results)
