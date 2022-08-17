#1C:\EGARCIA\IT_Automation_w_Python python
import C2_Module

def operations():
    i = 0

    while i<10:
        print("Hello world...")
        i += 1

    i= 0
    print("\n")

    for i in range(10):
        print("Hello again...")
        i += 1
    return 0

def readFile(fileName):
    file = open(fileName)
    text = file.read()
    print("Content of the file:\n", text)
    return 1

#operations()
#readFile("Text.txt")
#text = C2_Module.inputText("Enter text:")
bigRadius = input("Enter big radius: ")
smallRadius = input("Enter small radius: ")
area = C2_Module.donutArea(bigRadius, smallRadius)
print("Donut area --> {}".format(area))
