medicalCause = input('Did you have medical cause for you to miss exam(Yes/No)').lower()
atten = int(input("Enter the attendance of the student: "))
if medicalCause =="yes":
    print("You are allowed to redo your exam")
else:
    if atten >= 75:
        print("You are allowed to take exam")
    else:
        print("You're are not allowed to take exam")        
