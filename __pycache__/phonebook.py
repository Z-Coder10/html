#import module
import sys

def initial_phonebook():
    rows,cols =int(input("Please enter initial number of contacts:")),5
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
                   
                   phone_book.append(temp)
                   print(phone_book)
                   return phone_book
               
               def menu():
                   print("*********************************************")
                   print("\t\t\tSmartphone directory", flush = False)
                   print("***************************")
                   print("\tYou can now peform the following operations on this phonebook\n")
                   print("1. Add new Contact")
                   print("2. remove existing contact ")
                   print("3. Delete all contacts")
                   print('4. Search for a Contact')
                   print("5. Display all contacts")
                   print("6. Exit phonebook")
                   choice = int(input("Please enter your choice: "))
                   return choice
               
               def add_contact(pb):
                   dip =[]
                   for i in range(len(pb[0])):
                       if i == 0:
                           dip.append(str(input("Enter your name")))
                           if i ==1:
                               dip.append(int(input("Enter your Number")))
                               if i == 2:
                                   dip.append(str(input("Enter your Email")))
                                   if i == 3:
                                        dip.append(str(input("Enter your date of birth")))
                               if i == 4:
                                   dip.append(str(input("Enter your category")))
                                   
                                   if i == 5:
                                       dip.append(str(input("Enter category(family/friends/work/others): ")))
                                       pb.append(dip)
                                       return pb
                                   
                                   def remove_existing(pb):
                                       query = str(input("Please enter name of contact you wish remove from phonebook"))
                                       temp = 0
                                       for i in range(len(pb)):
                                           if query == pb[i][[0]]
                                           temp+=1
                                           print(pb.pop(i))
                                           if temp == 0
                                           print("Sorry, you have entered invalid query.\nPlease recheck and try it again")
                                           return pb
                                       initial_phonebook()
                                       menu()
                                       add_contact()
                                       remove_existing
                                       
                           