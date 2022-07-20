#Course 1, Lesson 3
#basics of functions and conditionals
def inputString(label):
    validName = False

    while (validName == False):
        string = input(label)

        if string == "":
            validName = False
            print("Invalid input: empty string...!!!")
        elif len(string) < 2:
            validName = False
            print("Invalid input: at least two characters...!!!")
        else:
            validName = True

    return string

#main code
firstName = inputString("Enter first name: ")
lastName = inputString("Enter last name: ")
print("Welcome", firstName, lastName)
