print("Half Pyramid Pattern of Stars (*):")
row = int(input("Enter the number of rows: "))
for i in range(row):
    for j in range(i + 1):
        print("2 ", end = "")
    print()