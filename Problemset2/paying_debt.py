# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:16:48 2020

@author: Tim de Boer
"""

def paying_debt(b, IR_annual, payrate_monthly):
    IR_monthly = IR_annual/12.0
    i = 1
    while i <= 12 :
        min_pay_monthly = payrate_monthly * b
        ub = b - min_pay_monthly
        b = ub + (IR_monthly * ub)
        print ('Remainig balance: ' + str(round(b,2)))
        i += 1
'''
IR_monthly = annualInterestRate/12.0
i = 1
while i <= 12 :
    min_pay_monthly = monthlyPaymentRate * balance
    ub = balance - min_pay_monthly
    balance = ub + (IR_monthly * ub)
    i += 1
print ('Remaining balance: ' + str(round(balance,2)))
'''