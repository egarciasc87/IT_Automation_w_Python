#this file is a module that contains functions
#that might be used by different scripts
import math

def readFile(fileName):
    file = open(fileName)
    text = file.read()
    return Text

def inputText(label):
    text = input(label)
    return text

def triangleArea(base, height):
    return base*height/2

def rectangleArea(base, height):
    return base*height

def circleArea(radius):
    return math.pi*(radius**2)

def donutArea(bigRadius, smallRadius):
    finalArea = 0

    if bigRadius.isnumeric() == False or smallRadius.isnumeric() == False:
        print("ERROR: values must be numeric.")
    elif bigRadius>smallRadius:
        smallArea = math.pi*(int(smallRadius)**2)
        bigArea = math.pi*(int(bigRadius)**2)
        finalArea = bigArea - smallArea
    else:
        print("Error: big radius must be larger.")

    return finalArea
