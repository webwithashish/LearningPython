day=int(input("enter a day"))
if day==1 or day==2 or day==3 or day==4 or day==5:
    print("weekday")
elif day==6 or day==7:
    print("weekend")
else:
    print("invalid")