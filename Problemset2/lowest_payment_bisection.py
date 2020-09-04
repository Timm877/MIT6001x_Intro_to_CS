# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:01:40 2020

@author: Tim de Boer
"""

balance_org = balance
# Paste your code into this box
IR_monthly = annualInterestRate/12.0


lower_bound_pay = balance / 12
upper_bound_pay = (balance*(1+IR_monthly)**12)/12
epsilon = 0.01

fixed_pay_monthly = (upper_bound_pay+lower_bound_pay)/2

while True:    
    for i in range(1,13):
        ub = balance - fixed_pay_monthly
        balance = ub + (IR_monthly * ub)
                
    if balance > 0 and balance > epsilon:
        lower_bound_pay = fixed_pay_monthly
        balance = balance_org
            
    elif balance < 0 and balance < -epsilon:
        balance = balance_org
        upper_bound_pay = fixed_pay_monthly
            
    else:
        print('Lowest Payment: ' + str(round(fixed_pay_monthly,2))) 
        break    
    fixed_pay_monthly = ((upper_bound_pay+lower_bound_pay)/2)
   