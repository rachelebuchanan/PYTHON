#RBuchanan_battingaverage.py
#Written by: Rachel Buchanan
#Date: 1/22/2023
#Prog Assignment Number 1
#
#Program Description
#       A simple program to calculate batting average.
#       Illustrates use of multiple input.
#
#Variables
#       playername - name of player
#       hits - number of hits
#       atbats - number of at bats
#       average - average of hits and at bats

def main ( ):

#Input - player name, get hits and at bats
        print ("The program computes the batting average of a baseball player.")
        name = input("What is the name of the baseball player? ")	 
        hits = eval(input("Enter the number of hits: "))
        atbats = eval(input("Enter the number of at bats: "))

#Process - player name, calculate the average
        average = hits / atbats
        
#Output - print the player name and average
        print("The batting average is: ", average)
        print(name , "has a batting average of ",average) 

main()


= RESTART: C:/Users/rache/OneDrive/Desktop/MGU GRAD/INTRO PROGRAMMING SPRING 2023/PYTHON IDLE/RBuchanan_battingaverage.py
The program computes the batting average of a baseball player.
What is the name of the baseball player? Abbot
Enter the number of hits: 125
Enter the number of atbats: 500
The batting average is:  0.25
Abbot has a batting average of  0.25

= RESTART: C:/Users/rache/OneDrive/Desktop/MGU GRAD/INTRO PROGRAMMING SPRING 2023/PYTHON IDLE/RBuchanan_battingaverage.py
The program computes the batting average of a baseball player.
What is the name of the baseball player? Abbot
Enter the number of hits: 125
Enter the number of at bats: 500
The batting average is:  0.25
Abbot has a batting average of  0.25
