li = ['apple','mango','avocado']
obj1 = enumerate(li)
print(list(obj1))

class Employee:
    def __init__(self):
        print("Employee was created")
        
    def __del__(self):
        print("The created employee was destroyed")
def create_job():
    print("Making Object...")
    obj = Employee()
    print("Function end..")
    return obj
print("Calling create-obj() function ...")
obj =create_job()
print("Program ends...")             