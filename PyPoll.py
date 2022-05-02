# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The Total number of votes each candidate received
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# Import the datetime class from the datetime module.
import datetime
from tkinter import messagebox
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Setup
# 1a. Initialize Counters and Trackers.
total_votes = 0
winning_count = 0
loop_counter = 0

winning_candidate = ""
winning_percentage = 0
largest_county_turnout = ""
largest_county_vote = 0

# Candidate and County Options
# 1b. Lists
candidate_options = []
county_names = []

# 1c. Dictionary
candidate_votes = {}
county_votes = {}

# 3. Process Election Results
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name and county name from each row.
        candidate_name = row[2]
        county_name = row[1]
        # loop_counter += 1
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
                
        # Begin tracking that print's vote count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        if county_name not in county_names:
    
            # Add the existing county to the list of counties.
            county_names.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Saves results to text file.
with open(file_to_save, "w") as txt_file:
     # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"----------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------------------\n\n"
        f"County Votes:\n")

    # Print to terminal    
    print(election_results, end="")

    # Saves results to text file.
    txt_file.write(election_results)

    # Loop to get the county from the county dictionary.
    for county in county_votes:
        # Retrieve the county vote count.
        county_vote = county_votes[county]
        # Calculate the percentage of votes for the county.
        county_percent = float(county_vote) / float(total_votes) * 100

        # Print the county results to the terminal.
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n")
        print(county_results, end="")

        # Saves results to text file.
        txt_file.write(county_results)

        # Determine the winning county and get its vote count.
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

    # Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
        f"\n----------------------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"----------------------------------------\n")

    # Print to Terminal
    print(largest_county_turnout)

    # Saves results to text file.
    txt_file.write(largest_county_turnout)

    # Loop to determine the percentage of votes for each candidate.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        # Saves results to text file.
        txt_file.write(candidate_results)
       
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

# Prints the winning candidate to terminal
    winning_candidate_summary = (
        f"----------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------------\n")
# Prints Winning Candidate Summmary   
    print(winning_candidate_summary) 

# Saves results to text file.
    txt_file.write(winning_candidate_summary)