#Course 1, Lesson 3
#basics of functions and conditionals
import datetime

def inputString(label, min, max):
    validName = False

    while (validName == False):
        string = input(label)

        if string == "":
            validName = False
            print("Invalid input: empty string...!!!")
        elif len(string) < min:
            validName = False
            print("Invalid input: at least ", min, " characters...!!!")
        elif len(string) > max:
            validName = False
            print("Invalid input: no more than ", max, " characters...!!!")
        else:
            validName = True

    return string

def inputYear():
    validYear = False
    year = 0

    while (validYear == False):
        string = input("Enter birth year: ")

        if string.isnumeric() == False:
            validYear = False
            print("Invalid input: enter a number...!!!")
        elif int(string) <= 1900:
            validYear = False
            print("Invalid input: must be bigger than 1900...!!!")
        elif int(string) > datetime.datetime.now().year:
            validYear = False
            print("Invalid input: not bigger than current year...!!!")
        else:
            validYear = True

    return int(string)


#main code
firstName = inputString("Enter first name: ", 2, 25)
lastName = inputString("Enter last name: ", 2, 25)
username = inputString("Enter username:", 8, 15)
yearBirth = inputYear()
print("\nWelcome", firstName, lastName)
print("Username-->", username)
print("Birth year-->", yearBirth)
