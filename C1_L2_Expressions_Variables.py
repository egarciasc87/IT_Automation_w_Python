import datetime

firtName = ""
lastName = ""
yearBirth = 0

firtName = input("Enter first name: ")
lastName = input("Enter last name: ")
yearBirth = input("Year of birth: ")
dateToday = datetime.datetime.now()
yearToday = dateToday.year

print("Full name:", firtName + " " + lastName)
print("Your age is supposed to be:", yearToday - int(yearBirth))
print("Today date:", dateToday)
print("Today: year->", dateToday.year, ", month->", dateToday.month, ", day->", dateToday.day)

variable = input("\nEnter whatever you want: ")
print("You entered a: ", type(variable))
