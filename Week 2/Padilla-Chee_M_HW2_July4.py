#Week 2 Assignment Mario Padilla-Chee

#Question 1: Write statement that counts the number of space characters in a string.

User_String=input("Please enter a statement sentence. The program will return the number of space characters in it:") #Prompts user to enter a sentence
User_ListString=list(User_String)
print("The number of spaces in your statement is: ", User_ListString.count(" ")) #Prints out a statement that counts the number of spaces using the count function
print("End of Question 1")
#%%
#Question 2: 
#Create a program that makes an empty list and adds 3 inputs from the user to populate the list
print("This program will start with an empty list and add 3 items the user defines, one at a time")
User_List=[]                                                                                                    #Creates an empty list named User_List
print(User_List)                                                                                                #Prints empty list
Item1=input("Please enter the first item to add to the list. It can be a number, string, tuple, or list:")      #Prompts user to input item 1
User_List.append(Item1)                                                                                         #Extends the list and adds item 1
print(User_List)                                                                                                #Prints current list
Item2=input("Please enter the second item to add to the list. It can be a number, string, tuple, or list:")     #Prompts user to input item 2
User_List.append(Item2)                                                                                         #Extends the list and adds item 2
print(User_List)                                                                                                #Prints current list
Item3=input("Please enter the third item to add to the list. It can be a number, string, tuple, or list:")      #Prompts user to input item 3
User_List.append(Item3)                                                                                         #Extends the list and adds item 3
print("Your final list is:",User_List)                                                                          #Prints final list
print("End of Question 2")
#%%

#Question 3

#This question asks the user to choose an arithmetic operator (+,-,*,/) and applies that operator to 2 defined numbers X and Y.

print("This program allows the user to input apply an arithmetic operator to 2 numbers (x and y).")
x=input("Please choose a value for x: ") #Prompts user to define x
y=input("Please choose a value for y: ") #Prompts user to define y
Operation=input("Please choose an arithmetic operator (+,-,*,/) to be applied on x and y in that order: ") #Prompts user to define the operator
if Operation == "+":                                  #if statement that is evaluated if user chooses addition
   Result=float(x)+float(y)
   print("The sum of",x,"and",y,"is",Result)
elif Operation == "-":                                #if statement that is evaluated if user chooses subtraction
   Result=float(x)-float(y)
   print("The difference of",x,"and",y,"is",Result)
elif Operation == "*":                                #if statement that is evaluated if user chooses multiplication
   Result=float(x)*float(y)
   print("The product of",x,"and",y,"is",Result)
elif Operation == "/":                                #if statement that is evaluated if user chooses division
   Result=float(x)/float(y)
   print("The quotient of",x,"and",y,"is",Result)
print("End of Question 3")
#%%
#Question 4

#Write a program that accepts the lengths of three sides of a triangle as inputs and indicates whether the triangle is equilateral

print("This program asks the user to input the lengths of a triangle and determine whether the triangle is equilateral")
Side1=input("Please enter the dimensions of Side 1: ") #Prompts user to define triangle side 1
Side2=input("Please enter the dimensions of Side 2: ") #Prompts user to define triangle side 2
Side3=input("Please enter the dimensions of Side 3: ") #Prompts user to define triangle side 3

if float(Side1)==float(Side2) and float(Side2)==float(Side3) and float(Side3)==float(Side1): #Use float for all of them since not using it would cause 2 and 2.0 to be different lengths
    print ("The triangle is equilateral")
else:                                                                                        #Else statement if sides aren't all equal to each other
    print("The triangle is not equilateral")
print("End of Question 4")
#%%
#Question 5
print("This program approximates the value of pi/4 based on the number of iterations in a series the user determines will be evaluated")

elements=input("Please type in as an integer, the number of elements in the Leibniz series to evaluate(up to 17): ")             #Prompts user to enter number of elements in the Leibniz series to evaluate
Leibniz=[1,-(1/3),(1/5),-(1/7),(1/9),-(1/11),(1/13),-(1/15),(1/17),-(1/19),(1/21),-(1/23),(1/25),-(1/27),(1/29),-(1/31),(1/33)]  #List containing the first 17 elements in the Leibniz series
Summation=sum(Leibniz[:int(elements)])                                                                                           #Sums up value of new list, resulting from the slicing of original array, based on how many elements user chooses

print("The value of pi/4 using", elements,"elements in the infinite series is ", Summation)                                      #Prints value of summation

print("End of assignment")



    

    


