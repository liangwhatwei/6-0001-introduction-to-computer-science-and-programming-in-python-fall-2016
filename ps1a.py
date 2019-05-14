# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:58:56 2019

@author: liangwhatwei
"""
annual_salary = int(input("Enter your annual salary: ")) #ask user to input their amount of annual salary
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) #ask user to input the amount of portion of salary to be saved
totalcost = int(input("Enter the cost of your dream home: ")) #ask user to input cost of dream house
portion_down_payment = 0.25*totalcost #calculate the down payment of dream house
current_savings = 0 #starts with current savings of $0
month = 0 #starts the number of months needed to save for downpayment as 0
r = 0.04 #the annual return for investments
while current_savings<portion_down_payment: #if current savings is more than downpayment, stop
    current_savings = current_savings+((portion_saved*annual_salary)/12)+((r*current_savings)/12) #to calculate the total amount of savings added per months
    month = month + 1 #calculate the amount of months needed for downpayment
print ("\nNumber of months:",month) #print the number of months needed for down payment