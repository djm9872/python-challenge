#import modules
import os
import csv

#create path to file
csvpath = os.path.join("Resources", "budget_data.csv")


#open the csv file
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")


#skip the header row and create list holders
    csv_header = next(csvreader)
    revenue = []
    date = []
    rev_change = []
    

#read through each row and get sum of rows and total sum
    for row in csvreader:
        revenue.append(int(row[1]))
        date.append(row[0])
        
    print("Financial Analysis")
    print("______________________________")
    print(f"Total Months: {len(date)}")
    print(f"Total: ${sum(revenue)}")

    for i in range(len(revenue)):    
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = float(sum(rev_change) / len(rev_change))

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])

        min_rev_change_date = str(date[rev_change.index(min(rev_change))])

    print(f"Average change in Revenue: ${round(avg_rev_change)}")
    print(f"Greatist Increase in Profits: {max_rev_change_date} ${max_rev_change}")
    print(f"Greatist Decrease in Profits: {min_rev_change_date} ${min_rev_change}")
    
        

    
    
        
    