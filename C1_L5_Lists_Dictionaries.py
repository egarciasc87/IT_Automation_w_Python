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


#example2: operations with lists
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

    listFruits = ['Orange', 'Pineapple',
        'Strawberry', 'Kiwi', 'Peach']
    print("List of fruits:", listFruits)
    print("Skip one element:", skip_elements(listFruits))

def listComprehension():
    languages = ["Python", "C#", "C++", "Java", "Basic"]
    newList1 = []
    newList2 = []

    #Method 1 (not list comprehension)
    for item in languages:
        newList1.append(len(item))

    #method 2: list comprehension
    newList2 = [len(item) for item in languages]

    print("Original list: {}".format(languages))
    print("Result of method 1:", newList1)
    print("Result of method 2:", newList2)

#example3: operations woth tuples
def tupleOperations1():
    fullname = ("Grace", "M", "Hooper")
    numberSeconds = input("Enter # of seconds: ")
    result = convertSeconds(numberSeconds)
    print("Result:", result)
    hours, minutes, seconds = result
    print("Detailes result: {}, {}, {}".format(hours, minutes, seconds))
    tuplePeople()

def tuplePeople():
    people = [("Erick", "Garcia", "M", "175"), ("Carlos", "vera", "M", "170"),
    ("Pedro", "Zamora", "M", "182")]

    print("\nTuple people:", people)

    for firstName, lastName, sex, height in people:
        print("Email ->", (firstName[0] + lastName + "@email.com").lower())

def tupleAnimals():
    animals = ["lion", "zebra", "dolphin", "dog", "cat"]
    charsLen = 0

    for i in animals:
        print("Item: ", i)
        charsLen += len(i)

    for index, item in enumerate(animals):
        print("{} - {}".format(index, item))

    print("Average of length:", charsLen/len(animals))
    print("Average of length:", charsLen/len(animals))

def convertSeconds(seconds):
    hours = int(seconds) // 3600
    minutes = (int(seconds) % 3600) // 60
    seconds = int(seconds) % 60
    return hours, minutes, seconds #<--- this is a tuples


#example4: operations with dictionaries
def dictionaryOperations1():
    list = ["Peru", "Holanda", "China"]
    tuple = [("Peru", "America", "Español"),
        ("Holanda", "Europa", "Holandez"),
        ("China", "Asia", "Chino")]
    dictionaryPeopleHeight = {}

    name = "XXX"
    height = 0
    while name != "":
        name = input("Enter name: ")

        if name == "":
            break

        height = input("Enter height: ")
        dictionaryPeopleHeight[name] = height

    print("List of items:", dictionaryPeopleHeight)

    for item in dictionaryPeopleHeight:
        print(item)

    for item, value in dictionaryPeopleHeight.items():
        print("{}'s height is {} cm.".format(item, value))

def countLetter():
    dictionaryCount = {}
    text = input("Enter text: ")

    for letter in text:
        print(letter)
        if letter not in dictionaryCount:
            dictionaryCount[letter] = 1
        else:
            dictionaryCount[letter] += 1

    print(dictionaryCount)
    print("Dictionary values:", dictionaryCount.values())
    print("Dictionary values:", dictionaryCount.keys())
    print("Dictionary items:", dictionaryCount.items())

#listOperations1()
#tupleOperations1()
#listComprehension()
#dictionaryOperations1()
countLetter()
