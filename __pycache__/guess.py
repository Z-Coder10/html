actual_cost = float(input("please enter actual product cost"))
sale_amount = float(input("Please enter the sales amount"))

loss = actual_cost - sale_amount

if(sale_amount >actual_cost):
    profit = sale_amount - actual_cost
    print("Total profit = {0}".format(profit))
    
else:
    print("Oops you got loss", loss)
num = int(input("Please enter a number to compare whether it is greater than 15."))
if(num  >15):
    print("The number is greater than 15")
    
elif(num == 15):
    print("The number is equal to 15")
        
else:
    print("The number is lesser than 15")