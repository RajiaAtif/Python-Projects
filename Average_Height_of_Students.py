#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:47:17 2023

@author: haider
"""
#for example you want to calculate avg height of students in a classroom
std_heights = input("Give a list of students heights separated by space: ").split()
for std in range(len(std_heights)):
    std_heights[std] = int(std_heights[std])
print(std_heights)
total_heights = sum(std_heights)
total_stds = len(std_heights)
avg_height = round(total_heights/total_stds)
print(avg_height)