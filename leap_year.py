#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:20:39 2023

@author: haider
"""

year = int(input("Please enter the year: "))
def leap_year(year):
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year}: leap year ")
            else:
                print(f"{year}: Not a leap year")
        else:
            print(f"{year}: leap year")
    else:
        print(f"{year}: Not a leap year")
        
leap_year(year)