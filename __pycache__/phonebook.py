#import module
import sys

def initial_phonebook():
    rows,cols =int(input("Please enter initial number of contacts:"))
    phone_book = []
    print(phone_book)
     
    for j in range(rows):
        print("\nEnter contact %d details in the following order(ONLY):%(i+1)")
        print("NOTE: * indicates mandatory fields")
        print('****************************************')
        temp = []
        if j in range(cols):
                if j  == 0:
                    temp. append(str(input("Enter name: ")))
                    if temp[j] =='' or temp[j]=='':
                        sys.exit("Name is mandatory field. process exit due to blank field")
        
        if j == 1:
            temp.append(int(input("Enter number: ")))
            
            if j == 2:
               temp.append(int(input("Enter e-mail address: ")))
               if temp[j] =='' or temp[j]==' ':
                   temp[j] = None
                   
                   if j == 3:
                       temp.append(int(input("Enter Date of Birth: ")))
               if temp[j] =='' or temp[j]==' ':
                   temp[j] = None
                   
                   if j == 4:
                       temp.append(int(input("Enter category(family/friends/work/others:): ")))
               if temp[j] =='' or temp[j]==' ':
                   temp[j] = None
                   
                   