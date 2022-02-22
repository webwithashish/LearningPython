# make list as student name with 5 unique name
# then take a name form user and check for name present in the string or not

student_name = ["ashish", "jon", "jose", "smith", "martin"]
uin = input("enter the name to check ")
for name in student_name:
    if uin == name:
        print("the name is present")
        break
    elif uin != name[-1]:
        print("name is not present in the list")
        print("for adding a name to the list type yes otherwise type no")
        uchoice = input("type yes / no ")
        if uchoice == "yes":
            # student_name.append(uin)
            new_element = input("enter the new name ")
            print("new name ", new_element, "is added to the list")
            student_name.append(new_element)
            print("modified list", student_name)
        elif uchoice == "no":
            print("name not added to the list")
        else:
            print("invalid user input")
        break

