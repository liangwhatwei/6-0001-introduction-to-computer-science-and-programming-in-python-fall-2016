# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:31:39 2019

@author: random
"""

annual_salary = int(input("Enter your annual salary: ")) #ask user to input their amount of annual salary
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) #ask user to input the amount of portion of salary to be saved
totalcost = int(input("Enter the cost of your dream home: ")) #ask user to input cost of dream house
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: ")) #ask user to input semi-annual raise

portion_down_payment = 0.25*totalcost #calculate the down payment of dream house
current_savings = 0 #starts with current savings of $0
month = 0 #starts the number of months needed to save for downpayment as 0
r = 0.04 #the annual return for investments

while current_savings<portion_down_payment: #if current savings is more than downpayment, stop
    current_savings = current_savings+((portion_saved*annual_salary)/12)+((r*current_savings)/12) #to calculate the total amount of savings added per months
    month = month + 1 #calculate the amount of months needed for downpayment
    
    if (month%6)==0: #to check if half of year have pass to be eligible for semi_annual raise
        annual_salary = annual_salary+(annual_salary*semi_annual_raise) #increase the annual_salary with semi_annual raise

print ("\nNumber of months:",month) #print the number of months needed for down payment