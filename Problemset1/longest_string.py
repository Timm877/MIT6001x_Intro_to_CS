# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:47:41 2020

@author: Tim de Boer
"""
s = 'fdjnjhgbjisdfghiosjdjgosd'
x = longest = ""

for char in s:
    x = x + char if x == "" or char >= x[-1] else char
    longest = x if len(x) > len(longest) else longest
    
print('Longest substring in alphabetical order is: ' + str(longest))
  