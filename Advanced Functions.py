# List comprehension
number = [1,2,4,6,7,8]
even = [x for x in number if x %2 == 0]
print('List of even number from numbers is: ',even)


# Dictionary Comprehension
myDict = {str(x):x**2 for x in [1,3,7,8,9,5]}
print(myDict)

#Map
def square(n):
    return n*n
number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
result = map(square,number)
print(list(result))


#Zip
name = ['Zakir','Fareed','David',"Kevin"]
grade = [3,5,7,10]
mapped = zip(name,grade)
print(list(mapped))

#Exit
ages = [18,45,12,78]
for age in ages:
    if age <18:
        print("You are not eligible to vote since you are", age, "years old")
        print(exit)
        exit()
    else:
        print("You are eligible to vote")    