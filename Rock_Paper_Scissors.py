#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:50:34 2023

@author: haider
"""
import random
import sys
choice = int(input("Rock, Paper, Scissors! Type 0 for Rock, 1 for Paper, 2 for Scissors"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
comp_choice = random.randint(0,2)
if not choice > 2 :
    print(images[choice])
    print(f"computer chose: {comp_choice}\n{images[comp_choice]}")
else:
    sys.exit("You entered wrong choice which is "+ str(choice))
if choice == 0 and comp_choice == 2:
    print(f"Computer chose {comp_choice}. You win")
elif choice < comp_choice:
    print(f"Computer chose {comp_choice}. You lose")
elif choice == comp_choice:
    print(f"{comp_choice}. It\' a draw.")
elif choice == 2 and comp_choice == 0:
    print(f"Computer chose {comp_choice}. You lose")
elif choice > comp_choice:
    print(f"Computer chose {comp_choice}. You win")
elif choice >= 3 or choice < 0:
    print("You entered wrong choice.")