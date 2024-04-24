def zellers_formula(year, month, day):
    """
    This function calculates the day of the week using Zeller's formula.

    :param year: int - the year
    :param month: int - the month (1-12)
    :param day: int - the day of the month (1-31)
    :return: str - the day of the week
    """
    if month < 3:
        month += 12
        year -= 1
    d = year % 100
    c = year // 100
    h = (day + ((13 * (month + 1)) // 5) + d + (d // 4) + (c // 4) + (5 * c)) % 7
    day_of_week = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
    }
    return day_of_week[h]

if __name__ == "__main__":
    date = int(input("Enter the date (1-31): "))
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))
    print("The day of the week is:", zellers_formula(year, month, date))ṁ