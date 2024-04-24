def check_prime(number):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                return False
        return True
    else:
        return False

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from user
num = int(input("Enter a number: "))

# Check if the number is prime
if check_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Check if the number is a leap year
if check_leap_year(num):
    print(f"{num} is a leap year.")
else:
    print(f"{num} is not a leap year.")