"""
Project Name: Mad Libs
Author: Chisonth Tharmapalan
Date: December 11, 2022
Description: Generates a mad lib text with some input from the user. Mad Libs from https://www.madtakes.com/ have been used.
"""
import random
gate = True


def answer_collector(display_prompt):
    answer = input(display_prompt)
    if answer == "-1":
        print("Thanks for playing!")
        gate = False
        
while gate:
    madlib_selector = random.randint(1,5)
    print(madlib_selector)
    



    