import os
import csv

# Variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

# Set Path & open file
csvpath = r'Resources\election_data.csv'
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read The Header Row 
    csv_header = next(csvfile)
    row = next(csvreader)

    # Task Begins
    for row in csvreader:
        
        # The total number of votes cast
        total_votes += 1
        
        # The total number of votes each candidate won
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        else:
            Otooley_votes += 1
        
    # The percentage of votes each candidate won
    Kahn_percent = Khan_votes / total_votes
    Correy_percent = Correy_votes / total_votes
    Li_percent = Li_votes / total_votes
    Otooley_percent = Otooley_votes / total_votes

    # The winner of the election based on popular vote
    winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)

    if winner == Khan_votes:
        winner = "Khan"
    elif winner == Correy_votes:
        winner = "Correy"
    elif winner == Li_votes:
        winner = "Li"
    else:
        winner = "O'Tooley" 

# Print
print(f"Election Results")
print(f"------------------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {Kahn_percent:.3%}({Khan_votes})")
print(f"Correy: {Correy_percent:.3%}({Correy_votes})")
print(f"Li: {Li_percent:.3%}({Li_votes})")
print(f"O'Tooley: {Otooley_percent:.3%}({Otooley_votes})")
print(f"------------------------------------------------")
print(f"Winner: {winner}")
print(f"------------------------------------------------")       

# Output
result = r'analysis\PyPoll_Result.text'
print(result)

with open(result, 'w',) as txtfile:

    # txtfile Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"------------------------------------------------\n")
    txtfile.write(f"Kahn: {Kahn_percent:.3%}({Khan_votes})\n")
    txtfile.write(f"Correy: {Correy_percent:.3%}({Correy_votes})\n")
    txtfile.write(f"Li: {Li_percent:.3%}({Li_votes})\n")
    txtfile.write(f"O'Tooley: {Otooley_percent:.3%}({Otooley_votes})\n")
    txtfile.write(f"------------------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"------------------------------------------------\n")
    
