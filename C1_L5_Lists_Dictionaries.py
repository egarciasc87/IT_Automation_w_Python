def HelloWorld(n):
    while n > 0:
        print("Hello World...!!!")
        n -= 1

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name, grade)

def stringOperations1():
    defaultNumber = 5
    string = input("Enter full name: ")
    indexSpace = string.index(" ")
    print(string)
    print(string.split())
    print("Nombre->",
        string[:indexSpace],
        ", Apellido->",
        string[indexSpace+1:])

    print("\n")
    HelloWorld(int(defaultNumber))

    print(student_grade("Reed", 80))
    print(student_grade("Paige", 92))
    print(student_grade("Jesse", 85))


#example1: replace old domain by new domain
def stringOperations2():
    old_domain = "email.ru"
    new_domain = "gmail.com"
    listEmails = ["egarcia@email.ru",
        "cgarate@email.ru",
        "gvera@email.ru"]
    newListEmail = []

    for email in listEmails:
        index = email.index("@")
        newEmail = email[:index + 1] + new_domain
        newListEmail.append(newEmail.upper())

    print("\nOld domain list:", listEmails)
    print("New domain list:", newListEmail)
    print(", ".join(newListEmail))
    print(" ".join(newListEmail))


#example2: list
def addIem(list, item, index):
    if index == 0:
        list.append(item)
    else:
        list.insert(index, item)
    return list

def removeItem(list, item):
    list.remove(item)
    return list

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for i in range(len(elements)):
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(elements[i])
		# Increment i
		i += 1

	return new_list

def listOperations1():
    string = "\nThis is a sentence in english language"
    print(string)
    listSentences = string.split()
    index = input("Location of the word to extract [1, 2, ...]: ")
    index = int(index)
    print("Result: {}".format(listSentences[index-1]))

    print(skip_elements(['Orange', 'Pineapple',
        'Strawberry', 'Kiwi', 'Peach']))
