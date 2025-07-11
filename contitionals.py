age = int(input("enter your age:"))


if age == 18:
    print("you are okay to drive")
elif age < 30:
    print("please using driving safety")
elif age > 30:
    print("you are greater than thirty")

else:
    print("you are not okay to drive")
