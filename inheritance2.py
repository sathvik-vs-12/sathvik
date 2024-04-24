class A:
  def mp(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
  
class B(A):
  def neon(a):
    if a==0 or a==1 or a==9:
      print("Neon number")
    else:
      print("Not a neon number")    
       
class C(A):
  def x(name):
        name =str(input("Enter name : "))
        length = len(name)
        for i in range(length):
            for j in range(length):
                if i==j or i+j==length-1:
                    print(name[i],end=" ")
                else:
                    print(" ",end= " ")
            print()

    
class E(B,C):
  def reverse(name):
    print(name[::-1])
obj=E   
obj.mp(11)
print(obj)
obj.neon(11)
obj.x("bitm")
obj.reverse("bitm")
    
    
    
    
    
    
    
    
    
'''   
class D(A):
  def banking(self): '''