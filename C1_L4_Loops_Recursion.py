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

print("Fibonacci list:", fibonacciList)
print("Length of the list:", len(fibonacciList))
print("Numbers added:", number)
