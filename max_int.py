#Create a program which finds the maximum number of all the prositive inputs.

num_int = int(input("Input a number: "))
#The user shall enter numbers until he enters a negative number.
#If a negative number is put in the program shall stop.
#The program shall print out the maximum number.

max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)
