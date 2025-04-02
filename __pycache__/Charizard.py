x = 5
if(type(x) is int):
    print("true")
else:
    print("false")    
print("Enter marks obtained in five subjects")
Math = int(input("Marks scored in Math"))
Science = int(input("Marks scored in Science"))
History = int(input("Marks scored in History"))
Quantitative = int(input("Marks scored in Quantitative"))
Technology = int(input("Marks scored in Technology"))
total = Math+Science+History+Quantitative+Technology
average = total/5
if average >= 90 and average <=100:
    print("Congratulations You got Grade A+. Your total mark is",total)