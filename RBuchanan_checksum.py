#RBuchanan_checksum.py
#Written by: Rachel Buchanan
#Date: 2/14/2023
#Prog Assignment Number 3
#
#Program Description
#       A simple program that prompts for a string of characters and outputs
#       the checksum where values of each character modulo 10
#
#Variables
#       checksum - ord(c)
#       string - characters
#
#
def main ( ):
#
#Input - enter a string of characters 
        print("The program computes the value of a string of characters.")
        print()
        string = input("Enter a string of letters, numbers or characters: ")
#
#Process - calculate the checksum as the sum of character values modulo 10
        checksum = sum(ord(c) for c in string) % 10
#
#Output - print the checksum value for string of characters 
        print(f"The checksum of '{string}' is {checksum}")

main() 
