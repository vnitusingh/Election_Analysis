# Add the dependencies
import csv
import os

# The data we need to retrieve

## Assign a variable for the file to load and the path.
#### file_to_load = 'resources\election_results.csv' - One way to do
file_to_load = os.path.join("resources","election_results.csv")

## Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
## Using the open() function with the "w" mode we will write data to the file.

## Initialize a total vote counter
total_votes = 0

## Candidate Options and candidate votes - declare empty list
candidate_options = []

## Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    
    ## Read the file object with the reader function
    file_reader = csv.reader(election_data)

    ## Print the header row.
    headers = next(file_reader)
    print(headers)

    
    for row in file_reader:
        ###1. The total number of votes cast
        total_votes += 1
    
        ###2. A complete list of candidates who received votes
        candidate_name = row[2]

        ####If candidate is not in the list, then add the candidate
        if candidate_name not in candidate_options:

            #### Add the candidate name
            candidate_options.append(candidate_name)

            #### Begin to track candidate's votes
            candidate_votes[candidate_name] = 0

         # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #3. The percentage of votes each candidate won
    ### 3.1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        ### 3.2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        ### 3.3 Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        ### 3.4. Print the candidate name and percentage of votes.
    
        #4. The winner of the election based on popular vote.
        # 4.1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 5.2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 5.3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name


    
        candidate_results = (f"{candidate_name}: received {vote_percentage: .1f}%  ({votes:,}) of the vote.\n")
        txt_file.write(candidate_results)

       # print(f"{candidate_name}: received {vote_percentage: .1f}%  ({votes:,})\n.")
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    txt_file.write(winning_candidate_summary)




