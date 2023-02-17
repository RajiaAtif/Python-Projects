#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:34:15 2023

@author: haider
"""

age = input("please enter your age: ")
age_int = int(age)
years_remaining = 90 - age_int
weeks = years_remaining * 52
days = years_remaining * 365

print(f"You hava {years_remaining} years, {weeks} weeks and {days} days left")


