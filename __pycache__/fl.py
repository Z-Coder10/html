# with open("file.txt", "r") as f:
#     f.write("Hello do you love coding")
with open('file.txt' , 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
    