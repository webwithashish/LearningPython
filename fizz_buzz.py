# take the number from user
# if the number is divisible by 3 print fizz
# if the number is divisible by 5 print buzz
# it the number is divisible by both 3 and 5 print fizz-buzz
# else just print the actual number

def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "Fizz-Buzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


print(fizz_buzz(number=15))
