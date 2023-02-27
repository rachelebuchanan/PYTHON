#RBuchanan_discountcalculator.py
#Written by: Rachel Buchanan
#Date: 2/21/2023
#Prog Assignment Number 4
#
#Program Description
#       A simple program that calculates the price of an item on sale given the 
#       regular price and sales percentage.
#
#Variables
#       itemprice = the regular price of the item
#       percentagediscount = the sales percentage
#       reducedprice = the item's discounted price
#       $ = price of item
#       % = sales percentage
#
def main ( ):
#
#Input - retrieve user inputs
        print("This program calculates the sale price of an item.")
#        
        itemprice = float(input("What is the regular price of the item? $"))
        percentagediscount = float(input("What is the percentage discount? %"))
#        
#
#Process - calculate reduced price of item
        reducedprice = itemprice - itemprice * percentagediscount / 100 
#    
#
#Output - display item's reduced price
        print("The item's discounted price is: ")
        print(reducedprice) 

main() 
