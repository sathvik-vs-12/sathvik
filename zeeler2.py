date = int(input("Enter the date : "))
month = int(input("Enter the month : "))
year = int(input("Enter the year: "))

if month < 3:
    month += 12
    year -= 1

d = year % 100
c = year // 100
if date >= 31:
        print("Invalid date")
else:
    h = (date + ((13 * (month + 1)) // 5) + d + (d // 4) + (c // 4) + (5 * c)) % 7
    days = {0: "Saturday",1: "Sunday",2: "Monday",3: "Tuesday",4: "Wednesday",5: "Thursday",6: "Friday"}
    print("The day of the week is:", days[h])