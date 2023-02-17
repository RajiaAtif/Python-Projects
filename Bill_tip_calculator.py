#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:50:06 2023

@author: haider
"""

print("Welcome to the Tip Calcultor")
bill = float(input("Please enter your total bill amount: $"))
people = int(input("Number of people you would split in: "))
tip = int(input("How much tip you would want to give? 10, 12, 15: "))
bill_tip = (tip/100) * bill + bill
bill_per_person = bill_tip / people
print(f"Total bill including tip: {bill_tip} and each person will pay {bill_per_person}") 

s1 = 'abc'
s2 = 'abcdef'
print(s2.__contains__(s1))