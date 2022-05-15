# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:44:12 2020

@author: mpadilla
"""

#HW 3
footer=("=")*80
print("Question 1: Translate for loops to while loops")

#for count in range (100):
#    print (count)

#A)
#print the numbers 0 to 99
counter_a=0
while counter_a < 100:
    print(counter_a)
    counter_a+=1
print(footer)
#B)
#for count in range (1, 101):     
#    print (count)

#print the numbers 1 to 100
counter_b=1
while counter_b < 101:
    print(counter_b)
    counter_b+=1
print(footer)
#C)
#for count in range (100, 0, –1):
#    print (count)

#print the numbers 100 to 1, decreasing by 1

counter_c=100
while counter_c > 0:
    print(counter_c)
    counter_c-=1

print ("\n\nEnd of Question 1")
print (footer)
#%%
print("Question 2: Greatest Common Divisor")

#User inputs below, must be different and non zero
Number_A=int(input("Please select a non-zero positive integer:"))  
Number_B=int(input("Please select a different non-zero positive integer:"))

if Number_A>Number_B:        #Sorts numbers to into larger and smaller category  
    Larger=Number_A
    Smaller=Number_B 
else:
    Larger=Number_B
    Smaller=Number_A   
temp=[]                     #Create an blank array to append remainders along the process
Remainder=Larger%Smaller    #Remainder from using MOD operation
if Remainder==0:
    print("The division of", Larger, "divided by", Smaller, "has a remainder of", Remainder)        #If Larger is a multiple of smaller, then GCD is equal to smaller
    print("The GCD is:", Smaller)
    
else:
    while  Remainder != 0:                                                                          #If Larger isn't a multiple of smaller, perform Eucladian algorithm until remainder not equal to 0
        print("The division of", Larger, "divided by", Smaller, "has a remainder of", Remainder)    #Print out the division taking place, explaining the steps
        temp.append(Remainder)
        Larger=Smaller
        Smaller=Remainder
        Remainder=Larger%Smaller        
    else:                                                                                           #Once remainder becomes zero stop dividing
        print("The division of", Larger, "divided by", Smaller, "has a remainder of", Remainder)    #Print out statement of final division in Eucladian algorithm
        print("The GCD is:",(temp[-1]))                                                             #Last entry in the temp remainder list is the GCD
print ("\n\nEnd of Question 2")
print(footer)
#%%
print("Question 3: Number entries Sum and Average")
entry=input("Please type in a number and press enter to add to list, or type anything but a number and press enter to finish list:")
summation=[]                                                                                        #Blank List to append down the line
summation.append(entry)                                                                             #Append First Value
while entry.isdigit()==True or entry.count(".")==1 or entry.count("-")==1:                          #while loop that allows user to keep inputing positive and negative integers and floats
    entry=input("Please type in a number and press enter to add to list, or type anything but a number and press enter to finish list:")
    summation.append(entry)
summation.pop()
summation_float=[]
for i in range(0,len(summation)):                                                                   #Change the series of number inputs to floats in order to perform calculations
    summation_float.append(float(summation[i]))
Final_Sum=sum(summation_float)                                                                      #Output of Final Sum    
Average=Final_Sum/float(len(summation_float))                                                       #Output of Average
                            
print("The final sum is {:.4f} and the average is {:.4f}".format(Final_Sum,Average))
print("\n\nEnd of Question 3")
print(footer)
#%%


#%%

#%%
print("Question 5:Payroll")

Employee_Inputs=[("Lambert", 34, 10.50), ("Osborne", 22, 6.25), ("Giacometti", 5, 100.70)]          #Input parameters of Payroll list
print(Employee_Inputs)                                                                              #Print list of inputs
print("{:*<25}{:*^10}{:*>45}".format('Last Name','Hours','Amount Paid in Period($)'))               #Table Headers
for i in range(0,len(Employee_Inputs)):
    print("{0:<25}{1:^10}{2:>45.2f}".format(Employee_Inputs[i][0],Employee_Inputs[i][1],(Employee_Inputs[i][1]*Employee_Inputs[i][2]))) #Printing of table data

print("\n\nEnd of Question 5")
print(footer)

#%%

print("Question 6: Concordance Tracking")
Poem="Never give in — Never, never, never, never, in nothing great or small, large or petty, never give in except to convictions of honour and good sense. Never yield to force; never yield to the apparently overwhelming might of the enemy. O horror, horror, horror. Words, words, word. But you never know now do you now do you now do you."
print(Poem)
Poem_lower=Poem.lower()
temp=[]
for i in range(0,len(Poem_lower)):  #Make a for loop to create a list of special characters in poem
    if Poem_lower[i].isalpha()==False:   #If statement checking for special characters
        temp.append(Poem_lower[i])       #If special character is detected appended to list
    else:
        pass     
temp_set=set(temp)                      #Turn list into set to spit out unique special character occurences
bad_char=list(temp_set)                 #Turn back into list and call it bad_char
bad_char.remove(" ")                    #Remove whitespace from bad char list. It will be used later in split function
for k in range(0,len(bad_char)):                    #Make a for loop to replace bad characters with empty ""
    update_poem=Poem_lower.replace(bad_char[k],"")
    Poem_lower=update_poem      #Poem with all lower case and every special character except whitespace removed at end of loop
Poem_split=Poem_lower.split()  #Split all words by the whitespace
poem_set=set(Poem_split)       #Turn string into set to get unique occurences
poem_unique_list=list(poem_set)       #Turn set into list to make it mutable
poem_unique_list.sort()               #Sort the words list into alphabetical order
#print(poem_unique_list)               #Sorted List of unique words in alphabetical order

concordance=[]
for j in range(0,len(poem_unique_list)):
    concordance.append(((poem_unique_list[j]),Poem_split.count(poem_unique_list[j])))
    print(((poem_unique_list[j]),Poem_split.count(poem_unique_list[j])))
print("\n\n\nConcordance List is Below")
print(concordance)

print("\n\nEnd of Assignment")
print(footer)

            
        

