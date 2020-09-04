# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:19:48 2020

@author: Tim de Boer

Script for calculating occurences of 'bob' in certain string s.
"""

s = 'examplestring'
n = 0
x = 0
while n+3 <= len(s)+1:
    if s[n:n+3] == 'bob':
        x += 1
    n +=1
print('Number of times bob occurs is: ' + str(x)) 