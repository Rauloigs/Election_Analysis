# Election_Analysis

## Overview of Election Audit: 

Along with Tom, the objective of this election audit analysis is to provide the Colorado Board of Elections with the results.
Before the Challenge the purpose was to go through the .csv file were all of the votation data is and expose the following:

1. Total number of votes cast.
2. A complete list of candidates who received votes.
3. Total number of votes each candidate received.
4. Percentage of votes each candidate won.
5. The winner of the election based on popular vote. 

These 5 mentioned points were meant to be exposed at a file that we created named election_analysis.txt. The output was the following: 

<img width="304" alt="PyPoll_Results" src="https://user-images.githubusercontent.com/84519822/149426840-e789b368-8e3a-463c-adbd-7a1c8d1bbe49.png">

Now the board wants us to provide them with 3 outputs more: 

1. The voter turnout for each county.
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout.


## Election-Audit Results: 

The purpose of our code was to expose the results in the terminal and in a text file named *election_analysis.txt* so the following image is the output of our code in the terminal:

<img width="280" alt="Terminal" src="https://user-images.githubusercontent.com/84519822/149559507-9884f4c1-5d78-4f6b-b690-f6cc58b9871b.png">

These same results than ran at the terminal are the same results projected in the text file, so lets take a look at the results in the .txt:

<img width="345" alt="Text_File" src="https://user-images.githubusercontent.com/84519822/149559671-63000bbc-2c6b-44da-a406-6eb0374ba7ca.png">

Now that you´ve seen the results in both "locations" lets go to specific details of the results:

- How many votes were cast in this congressional election?

**369,711** Votes 

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

**Jefferson**: 38,855
**Denver**:    306,055
**Arapahoe**:  24,801

- Which county had the largest number of votes?

**Denver** was de county with the largest number of votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

**Total of Votes: 369,711**
*Charles Casper Stockham:* 85,213
*Diana DeGette:*           272,892
*Raymon Anthony Doane:*    11,606

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The winner was **Diana DeGette** with **272,892** votes and with a **73.8%** of the total votes.

## Election-Audit Summary: 

As we´ve seen, this code works perfectly for our election audit, nevertheless could this same script work for any other elections? 
There might be several changes to be done in order to execute our program for any other election application, rather exposing all of those changes, we are presenting 2 modifications that might be helpful in the future to the board.

1. Load the proper file to the code.

First of all, and most importantly, we neeed to ask ourselves, what is the file that we are going to work to, so the proposal is to add an input to ask the user for the name of the file before the "*file_to_load = os.path.join("Resources", "election_results.csv")*" 

<img width="484" alt="Summary1" src="https://user-images.githubusercontent.com/84519822/149576751-4d0b0d30-db42-4ec5-9300-134688eba782.png">


So the code might be: *file = input("Write the name of the file to be analyze: ")* after this the "*file*" variable is the one to insert to the "*file_to_load*" to replace in this case "*election_results.csv*"

2. Select the name of the text file where the board wants to see the results

So we don´t re-write in the same file over and over thye idea here is the same as in point one, which is to ask the user with an *input()* to insert the name they want for the analysis. The folder where this file will be save willl remain the sameone (*analysis*).


