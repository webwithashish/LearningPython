# take a number from user and check for positive or neagetive number
num = int(input("enter a number "))
if num==0:
    print("entered number is zero")
elif num>0:
    print("entered number is positive")
elif num<0:
    print("entered number is neagetive")
else:
    print("invalid number")