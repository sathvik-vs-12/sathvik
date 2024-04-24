# program to find prime or not 
def is_prime(i):
    if i<= 1:
        return False
    for i in range(2, int(i**0.5) + 1): 
        if i % i == 0:
            return False
    return True

# Example usage:
number = int(input("Enter a number to check if it is prime or not: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    
# Python program to check if a year is a leap year or not

def is_leap_year(i):
    if i % 100 == 0:
        return i % 400 == 0
    else:
        return i % 4 == 0
      
i = int(input("Enter a year: "))

if is_leap_year(i):
    print(f"{i} is a leap year.")
else:
    print(f"{i } is not a leap year.")

