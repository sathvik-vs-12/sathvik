list=input("Enter numbers seperated by space :").split()
list=[int(x) for x in list]
ne=0
odd=0
even=0
for i in list:
    if i < 0 :
        ne+=i
    elif i%2 != 0:
        odd+=i
    else:
        even+=i
print("sum of negative number",ne)
print("sum of odd numbers",odd)
print("sum of even number",even)


    
  