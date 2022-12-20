"""
Project Name: Mad Libs
Author: Chisonth Tharmapalan
Date: December 11, 2022
Description: Generates a mad lib text with input from the user. 
Mad Libs from https://www.madtakes.com/ have been used.
"""
import random
gate1 = True

print("Welcome To Madlibs! Enter the prompts with a word and get a\
 Mad Lib text! If you want to play another game then input -1,\
 to end the game reply with -2.")

while gate1:
    
    gate2 = True
    
    #Open the text file with the madlib templates and prompts
    f = open("madlibs_list.txt", "r")
    madlibs_list = f.readlines()
    madlibs_index = []
    print(len(madlibs_list))
    #Adding the index of all the madlibs in an array
    for i in range(len(madlibs_list)):
        madlibs_list[i] = madlibs_list[i].replace("\n","")
        if madlibs_list[i].isnumeric():
            madlibs_index.append(i+1)
    
    #Choosing the madlib for the current game
    madlib_selector = random.randint(0,2)
    
    #Saving the indices of the current game 
    prompt_index = int(madlibs_index[madlib_selector])
    madlib_current = madlibs_list[prompt_index]
    
    while gate2:
        prompt_index += 1
        if prompt_index < len(madlibs_list):
            prompt = madlibs_list[prompt_index]
        else:
            prompt = "1"
        
        #In the text file we are at the next 
        if prompt.isnumeric():
            print("this is the end of the game")
            print(madlib_current)
            gate2 = False
        
        #If the prompt is alphabetical 
        else:
            user_input = input(madlibs_list[prompt_index]+ ": ")
            if user_input == "-1":
                gate2 = False
            elif user_input == "-2":
                print("Thanks for playing!")
                gate1 = False
                gate2 = False
            else:
                madlib_current = madlib_current.replace("[Word Not Submitted]", user_input, 1)
              