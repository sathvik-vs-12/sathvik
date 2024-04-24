
#1
# Read an integer from the user
num1 = int(input("Enter an integer: "))

# Read a float from the user
num2 = float(input("Enter a float: "))

# Add the two numbers
sum = num1 + num2

# Print the result
print("The sum of", num1, "and", num2, "is", sum)

#2
# Read name, age and address from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

# Print the name, age and address
print("Hello, your name is " + name)
print("Your age is " + str(age))
print("Your address is " + address)

#3
# Read principal amount, rate of interest and time from the user
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time: "))

# Calculate the simple interest
SI = (P * R * T) / 100

# Print the simple interest
print("The simple interest is: ", SI)

#4
# Print the output
print("Hal@python********")

#5
# Import the 'datetime' module to work with date and time
import datetime

# Get the current date
now = datetime.date.today()

# Display a message indicating what is being printed
print("This is today's date: ")

# Print the current date in a specific format
print(now.strftime("%Y-%m-%d"))
