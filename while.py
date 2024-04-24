name =str(input("Enter name :"))
length = len(name)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(name[i],end=" ")
        else:
            print(" ",end=" ")
    print()
