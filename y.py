name =str(input("Enter name : "))
length = len(name)
for row in range(length):
    for col in range(length):
        if((col==3 and row>1) or (row==col and col<3) or (row==0 and col==0)):
            print(name(row),end=" ")
        else:
            print(end=" ")
    print()