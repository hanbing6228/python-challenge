# import the os module
import os

# Module for reading CSV files
import csv

#set uo the cvs file path
election_csv = os.path.join('Resources', 'election_data.csv')
# Open CSV file
with open(election_csv, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    name_votes = {}
    total_votes = 0
    i = 0
    winner = str()
    # Read each row of data after the header
    for row in csvreader:  
        total_votes += 1
        name = row[2]
        if name in name_votes:
            votes = name_votes.get(name)
            name_votes.update({name : votes + 1})
        else:
            name_votes.update({name : 1})
    #print("name_votes")
    print("Election Results")
    print ("------------------------------")
    print(f"Total Votes:" ,total_votes)
    print ("------------------------------")
    for keys, values in name_votes.items():
        print(keys + ": " +  str(round(values/total_votes*100, 5))  + "% (" + str(values) + ")")
        
    winner = ""
    max_votes = 0
    i = 0
    for keys, values in name_votes.items():
        if i == 0:
            winner = keys
            max_votes = values
            i += 1
        else:
            if values > max_votes:
                winner = keys
    
    #print(winner)
    
    #print("name_votes")
    #print("Election Results")
    #print ("------------------------------")
    #print(f"Total Votes:" ,len(total_votes))
    #print ("------------------------------")
    #print (f"Khan:"  )
    #print (f"Correy:" )    
    #print (f"Li:"  )    
    #print (f"O'Tooley:", )        
    print ("------------------------------")
    print("Winner:" + winner)
    print ("------------------------------")


# Set variable for output file
    output_file = open("output.txt", "w")
    print(winner, file = output_file)
    output_file.close()