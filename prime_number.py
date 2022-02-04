#Greet the user
print("Welcome to Prime Number Program !")
#Ask the user to enter a number
number=int(input("Enter a number "))
#Assigned a variable value as False
flag=False
#Start the condition
for i in range(2,number):
    if number%i==0:
        flag=True
        break

if flag==True:
    print("Not a Prime Number")
else:
    print("Prime number")