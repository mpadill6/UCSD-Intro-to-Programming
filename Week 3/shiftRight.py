print("Question 4 Bit-Shift")
#rightshift
string=input("Please specify the starting binary number:")
Shift=int(input("Please specify the number of times your binary will be shifted to the right:"))
spliced=string.replace(""," ") #Need to add space in between numbers to slice later
spliced_list=list(spliced)     #Transform string to list
binary=spliced_list[1:len(spliced_list):2] #Slice list to remove the spaces in the list, i.e every other index
temp=1
for temp in range(0,Shift):
    del binary[-1]
    binary.insert(0,"0")
    temp=+1
final_binary="".join(binary)
print("You're rightshifted new binary is:",(final_binary))
