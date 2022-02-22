# A candidate is recruited based on following criteria:
# If male, age should be above 30 yrs and height above 160cm.
# If female, age should be above 25yrs and height above 155cm.

gen = input("Gender male/female ")
age = int(input("enter your age "))
height = float(input("enter your height in cm "))

if gen == "male" and age >= 30 and height >= 160:
    print("Congo !!! candidate selected ")
elif gen == "female" and age >= 25 and height >= 155:
    print("Congo !!! candidate selected ")
else:
    print("not selected based on selection criteria")
