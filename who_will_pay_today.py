#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:52:52 2023

@author: haider
"""
import random
names = input("Enter everyone\'s names separated by comma: ")
names = names.split(",")  #split() splits the string on the basis of characters' provided and make a list
rand_num = random.randint(0, len(names)-1)
print(f"{names[rand_num]} will be paying for the food today")

#----------simpler way-----------
#The below code uses a funcion called choice() from random module to directly fetch a random element from list
rand_choice = random.choice(names)
print(f"{rand_choice} will be paying for the food today")
