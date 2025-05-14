for x in range(10):
    if x % 20 ==0:
        print("Welcome to Codingal")
    elif x % 15 == 0:
        print("Coding helps  you create apps and websites")
    elif x % 5 == 0:
        pass
    else:
        print(x)
        
a = input("Enter a word ")
for i in a:
    
    if(i=="A"):
        print("A is found")
        break
    else:
        print("A is not found")        
        