#Course 1, Lesson 4
#basics of loops (while, for) and recursion

#example 1: to count repetitions
number = input("Number of repetitions: ")
i = 0

while i<int(number):
    print("Repetition", i)
    i = i +1


#example 2: add X numbers to fibonacci list
fibonacciList = [0, 1]
number = input("\nHow many number do you want to add? ")
number = int(number)
maxNumber = input("Enter max value for an item:")
maxNumber = int(maxNumber)
i = 0

while i<number:
    count = len(fibonacciList)
    newNumber = fibonacciList[count-1] + fibonacciList[count-2]

    if newNumber <= maxNumber:
        fibonacciList.append(newNumber)
        i += 1
    else:
        print("WARNING: item", newNumber, "will exceed limit!!!")
        break

number = i
print("Fibonacci list:", fibonacciList)
print("Length of the list:", len(fibonacciList))
print("Numbers added:", number)


#example3: read item from fibonacciList
i = 0
sum = 0

print("\nList of items, one by one:")

for i in range(len(fibonacciList)):
    sum += fibonacciList[i]
    print("Item #", str(i+1), ":", fibonacciList[i])

print("Sum of items of the list:", str(sum))


#example4: read limited number of items
start = input("\nStart index: ")
start = int(start)
end = input("End index: ")
end = int(end)

for i in range(start, end):
    print("Item #" + str(i+1) + ":", fibonacciList[i])


#example 5: list of matches in a football league
teamsList = ["Sporting Cristal", "Alianza Lima", "Universitario", "Manucci", "UCV", "Melgar"]

for local in teamsList:
    for visitor in teamsList:
        if local != visitor:
            print(local, "VS", visitor)
