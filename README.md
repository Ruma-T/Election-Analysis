# Election-Analysis

###Purpose

  A Colorado Board of Election employee has given the following tasks to complete the election audit of a recent local congressional election. We need to find the total votes cast, total number of votes for each candidate, the percentage of votes for each candidate, winner of the election based on the popular vote. We will help to automate the process by writing a code in python and generate a report. If that code runs successfully it  would be used in other districts elections too.

  1. Calculate the total number of votes cast: 369,711
  2. Get complete list of candidates who received votes:
	o  Charles Casper Stockham
	o  Diana DeGette
	o  Raymon Anthony Doane
      
  3.Calculate the total number of votes each candidate received
	• 	Charles Casper Stockham: 85,213

	•	Diana DeGette: 272,892

	•	Raymon Anthony Doane: 11,606
        
4. Calculate the percentage of votes each candidate won.
	•	Charles Casper Stockham: 23.0% 

	•	Diana DeGette: 73.8% 

	•	Raymon Anthony Doane: 3.1% 

Determine the winner of the election based on popular vote


	•	Winner: Diana DeGette
	•	Winning Vote Count: 272,892
	•	Winning Percentage: 73.8%


#Resources
	Data Source: election-results.csv
	-software: Python 3.9.6,Visual Studio Code-1.57.1

## Summary
  The analysis of the election show that:
      - There were 369,711 votes cast in the election.
    - The candidates were:
	o	Charles Casper Stockham
	o	Diana DeGette
	o	Raymon Anthony Doane
      
  -The candidate results were:
	o	Charles Casper Stockham received 23.0%  of the vote and 85,213 number of votes
	o	Diana DeGette received 73.8%  of the vote and 272,892 number of votes
	o	Raymon Anthony Doane received 3.1%  of the vote and 11,606 number of votes

   -The winner of the election was
  	-Diana DeGette received 73.8%  of the vote and 272,892 number of votes
	
	
Final resut will look like this in text form:

![png_Election Analysis](https://github.com/Ruma-T/Election-Analysis/blob/18560055d946bc35d4aa5f074a5fd7561af51752/Election%20Analysis.PNG)

## Challenges Overview
    We were given around 370,000 election data with ballot id, county name and candidate's name in a csv file.We had to read county wise votes cast to each candidate, count total votes for each candidate and total votes counted. Then calculate each candidate's percentage votes over total votes, compare candidate's total votes and get the winning candidate's name, total votes and percentage votes received.


## Challenges Summary
    We created a candidate votes dictionary with candidate options list.In the dictionary, we had candidate's name and votes as key and value. We set candidate's vote count to zero, and then we started tallying the votes for each candidate. We introduced .append to add candidate's name , if candidate's name was not in the list. After that, we counted the total number of all candidate's votes. We used loop variable to retrieve the votes of the candidate from the candidate_votes dictionary . Next, printed each candidate's name     and the percentage of votes using f-string formatting. This "f"Winning Percentage: {winning_percentage:.1f}%\n"print(winning_candidate_summary)" f-string was used to round to one decimal place and to start a new line

    Finally, we got the winning candidate Diana DeGette with total vote of 272,892 and her winning percentage was 73.8%.
    
  

##Election Audit Summary


The code we created in python could be used for any other elections with the different csv file. Such as if we want to analyze El Paso, Boulder, and Douglus county, we can use different CSV file with election data and analyze within few minutes. For the whole state this could be done within a short period of time. Even three types of data collected through ballot, in-person and any other type of vote could be analyzed separately to get better understanding of the whole process.


Example of Change in CSV file to load and the results will be like this :

 ![png_Electon_Analysis](https://github.com/Ruma-T/Election-Analysis/blob/db0e81080abe6c2f49250d2429a1434c79f2b260/election%20CSV.PNG)

![png_Electon-EBD](https://github.com/Ruma-T/Election-Analysis/blob/8a23cdd2a6c2490ab263b93a8136db42409ffef9/Election-EBD.PNG)

Results will be different in the colored part for any other election:

![png_Electon Results for any County](https://github.com/Ruma-T/Election-Analysis/blob/18560055d946bc35d4aa5f074a5fd7561af51752/Election%20Results%20for%20any%20County.png)

