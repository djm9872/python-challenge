#import modules
import os
import csv

#create path to file

csvpath = os.path.join("Resources","election_data.csv")

#open file

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

#skip the header row
    header = next(csvreader)

#create lists to compile 
    votes = []
    candidates = []
    khan = []
    correy = []
    li = []
    o_tooley = []

#loop through rows in csvreader and store voter id's in vote list and candidate names in candidate list

    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

#loop through names in candidate list and store each name to their own respective list

    for name in candidates:
        if name == "Khan":
            khan.append(name)
        elif name == "Correy":
            correy.append(name)
        elif name == "Li":
            li.append(name)
        elif name == "O'Tooley":
            o_tooley.append(name)

#calculate the percentages of each candidate to the total and round
    khan_perct = round(((len(khan) / len(votes))*100),2)
    
    cor_perct = round(((len(correy) / len(votes))*100),2)

    li_perct = round(((len(li) / len(votes))*100),2)

    o_perct = round(((len(o_tooley) / len(votes))*100),2)
    
    
    print("Election Results")  
    print("--------------------------")
    print(f"Total Votes: {len(votes)}")
    print("--------------------------")
    print(f"Khan: {khan_perct}% ({len(khan)})")
    print(f"Correy: {cor_perct}% ({len(correy)})")
    print(f"Li: {li_perct}% ({len(li)})")
    print(f"O'Tooley: {o_perct}% ({len(o_tooley)})")
    print("--------------------------")

#if statement to dynamically select the winner

    if khan_perct > cor_perct and khan_perct > li_perct and khan_perct > o_perct:
        print("Winner: Khan")
    elif cor_perct > khan_perct and cor_perct > li_perct and cor_perct > o_perct:
        print("Winner: Correy")
    elif li_perct > khan_perct and li_perct > cor_perct and li_perct > o_perct:
        print("Winner: Li")
    elif o_perct > khan_perct and o_perct > cor_perct and o_perct >li_perct:
        print("Winner: O'Tooley")

    print("---------------------------")
