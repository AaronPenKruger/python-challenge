# PyPoll folder
"""
Aaron PenKruger
"python-challenge 'PyPoll'" Due 3/21/2024

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

"""

#Import Modules
import os
import csv


#Create Path to collect election_data.csv

election_data_path = os.path.join("..", "Resources", "election_data.csv")

with open(election_data_path, "r") as csvfile:

    #Split the Data at the Commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip Header
    header = next(csvreader)

    

    # Initialize Dictionary to store cantidates and their votes 
    candidate_dict= {}    
    total_votes = int(0)
    election_winner= None
    highest_count = 0

    #For loop to iterate over rows and count votes 
    for row in csvreader:

        # Sum total votes
        total_votes += 1

        #Initialize Variables Within for-loop
        candidate_name = str(row[2])

        #Add name to list or add +1 vote to name
        if candidate_name not in candidate_dict:
            candidate_dict[candidate_name] = int(1)

        else: candidate_dict[candidate_name] += 1

   
    # Second For loop to calculate percentages and declare winner
    for candidate, votes in candidate_dict.items():
        vote_percent = round((votes /total_votes) * 100, 3)
        candidate_dict[candidate] = {"Votes": votes, "Percent of Total": vote_percent}


        # Find winner by highest count of votes 
        if election_winner is None: 
            election_winner = candidate
            highest_count = votes
        else:
            if highest_count < votes:
                highest_count = votes
                election_winner = candidate




    #Create Variable for output String to print and export 
                
        # Initiate String               
    output_string = \
        f"\nElection Results \n\n----------------- \n\nTotal Votes: {total_votes}\n\n-----------------\n\n"
    
        # For Loop to Add Dictionary of Candidates, Percentages and Votes to String
    for candidate, info in candidate_dict.items():
        output_string += f"{candidate}: {info['Percent of Total']}% ({info['Votes']}) \n"

        # Add Winner to String
    output_string += f"\n-------------- \n\nWinner: {election_winner} \n\n---------------"

    print(output_string)

    #Create txt file
    output_file_path = "election_results.txt"

    with open(output_file_path, 'w') as output_file:
        output_file.write(output_string)


