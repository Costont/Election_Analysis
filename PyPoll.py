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

# Open the election results and read the file.
with open(file_to_load) as election_data:
 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 # Read and print the header row.
    headers = next(file_reader)
    print(headers)
# Print each row in the CSV file.
    

    
    



    # To do: read and analyze the data here.























