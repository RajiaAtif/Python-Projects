#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:35:57 2023

@author: haider
"""

print("Welcome to your fave pizza delivery service\n")
size = input("Please choose your size from the followinf options: S/M/L: ")
add_pepperoni = input("Would you like pepperoni on top? Y/N: ")
add_cheese = input("Would you like extra cheese on top? Y/N: ")
total_bill = 0

if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
elif size == "L":
    total_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3
if add_cheese == "Y":
    total_bill += 1

print(f"Total bill: {total_bill}")