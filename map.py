#Exit
ages = [18,45,12,78]
for age in ages:
    if age <18:
        print("You are not eligible to vote since you are", age, "years old")
        print(exit)
        exit()
    else:
        print("You are eligible to vote since you are ", age, "years old")  