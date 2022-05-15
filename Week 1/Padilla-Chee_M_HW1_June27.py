#Assignment for Module 1 Due June 27th

#Question 1
#Write a Python program that prints (displays) your name, address, and telephone number.
print('Question 1: This section displays my name, address, and cell phone number')
print('My name is Mario Padilla-Chee') #Command printing my name
print('My address is 2844 Via Alta Place, San Diego, CA, 92108') #command printing my address
print('My Cell Phone number is 760-412-0113') #Command printing my cell phone number
print('End of Question 1')


#Question 2
#Write and test a program that computes the area of a circle.
#This program should request a number representing a radius as input from the user.
#It should use the formula 3.14 * radius ** 2 to compute the area and then output this result suitably labeled.

print('Question 2: This section calculates the area of a circle using an input radius from user')
#Request Input for radius of circle
radius=input("Enter the radius of your circle as a number:") #Tells user to input a desired radius for area calculation

#Compute Area of Circle
CIRCLE_AREA=3.14*float(radius)**2 #Formula for area of circle given a radius

#Display Calculated Area of Circle
print("The calculated area of the circle is:",CIRCLE_AREA, "units squared") #Display resulting area calculation
print('End of Question 2')

#Question 3
# Write and test a program that accepts the user’s name (as text) and age (as a number) as input.
#The program should output a sentence containing the user’s name and age.

print('Question 3: This section takes a name (text) and age (number) as input. Output should be a sentence containing user name and age')

#Request input for name (text) and age (number)

NAME=input("Enter your name as text:") #Requests user input their name as text
AGE=input("Enter your age as a number:") #Requests user input their age as number

print("Your name is",NAME,"and you are",AGE,"years old.") #Combines both inputs as a single sentence displaying name and age
print('End of Question 3')

#Question 4
#Write a program that calculates and prints the number of minutes in a year.

print('Question 4: This section calculates and prints the number of minutes in a year')
Minutes_Per_Hour=60 #Number of Minutes in 1 Hour
Hours_Per_Day=24    #Number of Hours in 1 Day
Days_Per_Year=365   #Number of Days in 1 Year

Minutes_Per_Year = Minutes_Per_Hour*Hours_Per_Day*Days_Per_Year

print('There are', Minutes_Per_Year,'minutes in a year.')
print('End of Question 4')


#Question 5
#Write a program that takes inputs for an employees hourly wage, total regular hours and total OT hours.
#It will then display an employee's total weekly pay.

print('This program calculates total weekly pay using input hourly wage, total regular hours worked, and total OT hours worked')

#Request Inputs for Salary Calculator
HOURLY_WAGE=input('Please input an hourly wage:') #Requests user to input an hourly wage
REGULAR_HOURS=input('Please enter the number of regular hours worked in a week:') #Requests user to input total regular hours worked
OT_HOURS=input('Please enter the total number of overtime hours worked in a week:') #Requests user to input total overtime hours worked

#Formula to Calculate Weekly Salary
Weekly_Salary=(float(REGULAR_HOURS)+(1.5*float(OT_HOURS)))*float(HOURLY_WAGE)

print("Your calculated weekly salary is: $"+str(Weekly_Salary)) #Prints out calculated weekly salary as statement
print("End of Assignment")

      



