# Election-Analysis

##Project Overview

  A Colorado Board of Election employee has given the following tasks to complete the elction audit of arecent  local congressional election

  1. Calculate the total number of votes cast : 369,711
  2. Get  complete list of candidates who received votes:
    	-Charles Casper Stockham
	    -Diana DeGette
	    -Raymon Anthony Doane
      
  3.Calculate the total number of votes each candidate received
        -Charles Casper Stockham: 85,213

        -Diana DeGette: 272,892

        -Raymon Anthony Doane: 11,606
        
4. Calculate the percentage of votes each candidate won.
        -Charles Casper Stockham: 23.0% 

        -Diana DeGette: 73.8% 

        -Raymon Anthony Doane: 3.1% 

Determine the winner of the election based on popular vote


        Winner: Diana DeGette
        Winning Vote Count: 272,892
        Winning Percentage: 73.8%


#Resources
      - Data Source: election-results.csv
      -software: Python 3.9.6,Visual Studio Code-1.57.1

## Summary
  The analysis of the election show that:
      - There were 369,711 votes cast in the election.
    - The candidates were:
	    -Charles Casper Stockham
	    -Diana DeGette
	    -Raymon Anthony Doane
      
  -The candidate results were:
	  -Charles Casper Stockham received 23.0%  of the vote and 85,213 number of votes
	  -Diana DeGette received 73.8%  of the vote and 272,892 number of votes
	  -Raymon Anthony Doane received 3.1%  of the vote and 11,606 number of votes
    
   -The winner of the election was
  	-Diana DeGette received 73.8%  of the vote and 272,892 number of votes

## Challenges Overview
    We were given around 370,000 election data with ballot id,county name and candidate's name in a csv file.We had to read county wise votes cast to each candidate,count total     votes for each candidate and total votes counted.Then calculate each candidate's percentage votes over total votes,compare candidate's total votes and get the winning           candidate's name, total votes and percentage votes received.


## Challenges Summary
    We created a candidate votes dictionary with candidate options list.In the dictionary, we had candidate's name and votes as key and value.We set candidate's vote count to         zero,and then we started tallying the votes for each candidate.We introduced .append to add candidate's name , if candidate's name was not in the list.Afterthat,counted         total number of all candidate's votes.Used loop variable to retrieve the votes of the candidate from the candidate_votes dictionary .Next,printed each candidate's name     and the percentage of votes using f-string formatting.This "f"Winning Percentage: {winning_percentage:.1f}%\n"print(winning_candidate_summary)" f-string was used to round to one     decimal place and to start a new line

    Finally we got the winning candidate Diana DeGette with toatl vote of 272,892 and her winning percentage was 73.8%.
