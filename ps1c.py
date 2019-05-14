# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:42:46 2019

@author: liangwhatwei
"""
starting_salary = int (input("Enter the starting salary: ")) #ask user to input starting salary
totalcost = 1000000 #cost of dream house
semi_annual_raise = 0.07 #semi-annual pay raise rate
r = 0.04 #annual investment rate
portion_down_payment = 0.25*totalcost #downpayment for dreamhouse
months = 36 #the number of months for the desired time to save up for downpayment

min_rate = 0 #0%
max_rate = 10000 #100%

portion_saved = int((max_rate+min_rate)/2) #bisection search formula
steps = 0 #no. of steps taken for bissection search
found = False #true/false whether if result found

while abs(min_rate-max_rate)>1: #while loop to check until min_rate and max_rate is same which mean a result is found
    steps += 1 #to find out how many steps is needed for bisection search
    annual_salary = starting_salary #to reset the annual_salary to starting_salary after each bisection search
    monthly_saved = (annual_salary/12.0)*(portion_saved/10000) #amount of money saved per month
    current_savings = 0.0 #set current_savings as 0
    
    for i in range(1, months+1): # from month 1 to month 36
        monthly_return = current_savings*(r/12) #monthly_return from investment
        current_savings = current_savings + monthly_return + monthly_saved #accumulated current savings from each month
        
        if abs(current_savings - portion_down_payment)<100: 
            min_rate = max_rate #to make break from while loop
            found = True #set found to True
            break #exit from loop
        elif current_savings > portion_down_payment + 100: 
            break #exit from loop
        
        if i%6 == 0: #to check if 6 months/12 months/18 months and so on for pay raise
            annual_salary = annual_salary + (annual_salary*semi_annual_raise) #increase pay
            monthly_saved = (annual_salary/12.0)*(portion_saved/10000) #increase monthly saved due to increase pay
    
    if current_savings<portion_down_payment - 100: 
        min_rate = portion_saved #set min rate as portion saved to eliminated the number below new min_rate
    elif current_savings>portion_down_payment + 100:
        max_rate = portion_saved #set max_rate as portion saved to eliminated the number above new max_rate
        
    portion_saved = int((max_rate + min_rate)/2) #bisection search
    
if found:
    print("Best savings rate:", portion_saved / 10000) #show best saving rates
    print("Steps in bisection search:", steps) #show number of steps taken for bisection search
else:
    print ("It is not possible to pay the down payment in three years.") #show the error
    