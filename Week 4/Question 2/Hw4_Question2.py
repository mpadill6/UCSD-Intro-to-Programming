#Question 2
import re

string="Please use my credit card number. It is Visa # 37562198673 with an expiration date of 08/19/2030. The CVS number is 854."
Number=[]
x=re.search("\s\d*\s",string) #Search for part of string where credit card numbers begin
for i in range(x.start()+1,x.end()-1): #Append each number of the into a list
    Number.append(int(string[i]))


temp=Number[-2::-2] #take numbers according to Luhn Algorithm using negative indices starting from rightmost
for j in range(len(temp)):
    sum_digit=0
    temp[j]=int(temp[j])*2  #Multiply Luhn numbers by 2
    if temp[j]>9:
        sum_digit=sum(int(digit) for digit in str(temp[j])) #add digits of Luhn numbers greater than 9
        temp[j]=sum_digit
    else:
        pass
#print(temp)
count=0
for m in range(1,len(temp)+1):
    Number[-2*m]=temp[count] #replace new Luhn numbers into the original array
    count+=1
#print(Number)
Sum_Credit_Card=sum(num for num in Number)
print("The Sum of the Luhm algorithm numbers is:",Sum_Credit_Card) #Sum numbers

if Sum_Credit_Card%10==0: #check if mod 10 = 0 for valid
    print("This is a valid Credit Card Number!")
else: #if number not divisible by 10, then output invalid
    print("This is an invalid Credit Card Number!")



    
    


