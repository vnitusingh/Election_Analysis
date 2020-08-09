# Election_Analysis

## Project Overview:
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentageof votes each candidate won.
5. Determine the winner of the election based on popular vote.

 
## Resources:
- Data Source: election_results.csv
- Software: Python 3.8.6, Visual Studio Code

## Election Audit Results:
The analysis of the election show that:
- There were **369,711** votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane


- The candidate results were:
  - **Charles Casper Stockham** received **23.0%** of the vote and **85,213** number of votes.
  - **Diana DeGette** received **73.8%** of the vote and **272,892** number of votes.
  - **Raymon Anthony Doane** received **3.1%** of the vote and **11,606** number of votes

- The winner of the election was:
  - **Diana DeGette**, who received **73.8%** of the vote and **272,892** number of votes.

## Election-Audit Summary:
The script already is designed to scale to any number of ballots or more candidates and counties. 
However, there is a scopr for improvement in the script. I would recommend following changes to the script:

- *Determine winner for each county:* In addition to determining which candidate won among all counties, I think it would also be helpful to determine how each candidate performed in every county.
- *User Inputs election data file:* Right now the data file for election is hard coded. In order to extend this script for any election, we can modify the script to accept the data file as user input.

