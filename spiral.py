tuple1 = ("zakir" , "Fareed" , "David" , False,3,5,5,10)
print(tuple1)
print(len(tuple1))
print(tuple1.count(5))
tuple2 = ("h",'g','y')
tuple3 = tuple2 + tuple1
print(tuple3)
print(tuple1[2])
print(tuple1[-1])
print(tuple1[1:4])


weather = (0,0,1,1,1,0,1,1)
sunny = 0
rainy = 0
for i in range(0,8):
    if(weather[i] == 0):
        rainy += 1
    else:
        sunny += 1
if(sunny > rainy):
    print("The weather is good today you don't need  your umbrella")
else:
    print("Please carry your Umbrella it's raining so much today")                    