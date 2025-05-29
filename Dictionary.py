square = {1:1,3:9,5:25,7:49, 9:81}
for i in square:
    print(square[i])
    
test_dict = {"Codingal":3,"is":2,'best':2,'coding':1}
print("The Original Dictionary : " + str(test_dict))
k = 2
res = 0
for key in test_dict:
    if test_dict[key]==k:
        res+=1
        
print("Frequency of k is : " + str(res))