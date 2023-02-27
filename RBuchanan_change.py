#RBuchanan_change.py
#Written by: Rachel Buchanan
#Date: 2/5/2023
#Prog Assignment Number 2
#
#Program Description
#       A simple program to calculate exact coin change.
#       Illustrates the use of integer division to determine remainder.
#
#Variables
#       quarters - amount to dispense in quarters
#       dimes - amount to dispense in dimes
#       nickels - amount to dispense in nickels
#       pennies - amount to dispense in pennies
#       c - user coin amount entered 

def main ( ):

#Input - enter a number between 0-99
    print("The program computes coin change.")
    print()
    c = int(input("Please enter an amount between 0-99: "))
    print()
    
    
#Process - calculate the amount of coin change
    print("The total value of your change is:")
    print() 
    print(c//25, "quarters ")
    c = c%25
    print(c//10, "dimes ")
    c = c%10
    print(c//5, "nickels ")
    c = c%5
    print(c//1, "pennies ")
    c = c%1
    print()
    
#Output - print the numerical value of each coin
    print("The amount of each coin is listed above.") 
                  
main() 
   
    
