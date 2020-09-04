# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:34:53 2020

@author: Tim de Boer
"""

balance = 120
annualInterestRate = 0.9


IR_monthly = annualInterestRate/12.0




def fixed_pay(fixed_pay_monthly):
    i = 1
    b = balance
    while i <= 12:
        ub = b - fixed_pay_monthly
        b = ub + (IR_monthly * ub)
        i += 1
    if b > 0:
        fixed_pay_monthly +=10
        return fixed_pay(fixed_pay_monthly)
    print('Lowest Payment: ' + str(fixed_pay_monthly)) 
    
fixed_pay(0)
   