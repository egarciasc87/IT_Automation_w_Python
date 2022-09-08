import os
import datetime
import csv

#managing files
def open_file_1():
    fileName = input("Enter name of the file:")
    file = open(fileName)
    #fileContent = file.read()
    #print(fileContent)
    lines = file.readlines()
    print(lines)
    file.close()
    print("\nFile closed manually")

def open_file_2():
    fileName = input("Enter name of the file:")
    with open(fileName) as file:
        #print(file.read())
        for line in file:
            print(line.strip().upper())

    print("\nFile closed automatically")

def read_many_files():
    index = 1

    for i in range(4):
        file = open("File_" + str(index) + ".txt")
        content = file.read()
        print(content)

def write_file():
    fileName = input("Enter file name:")
    openMode = "w"

    if file_exists(fileName) == True:
        openMode = "a"

    with open(fileName, openMode) as file:
        newContent = input("Enter new content:")
        file.write(newContent)

def remove_file():
    fileName = input("Enter file name:")

    if file_exists(fileName) == True:
        os.remove(fileName)
        print("File succesfully deleted!!!")
        return True
    else:
        return False

def rename_file():
    currentFileName = input("Enter current file name:")

    if file_exists(currentFileName) == True:
        newFileName = input("Enter file name:")
        os.rename(currentFileName, newFileName)
        print("File succesfully renamed!!!")
        return True
    else:
        return False

def file_exists(fileName):
    if fileName == "":
        fileName = input("Enter file name:")

    fileExists = os.path.exists(fileName)

    if fileExists == False:
        print("ERROR: file does not exist...")

    return fileExists

def get_file_data():
    fileName = input("Enter file name:")

    if file_exists(fileName) == True:
        size = os.path.getsize(fileName)
        dateModified = os.path.getmtime(fileName)
        absolutePath = os.path.abspath(fileName)
        print("File size: {} MB".format(size))
        print("Last time modified: {}".format(dateModified))
        print("Absolute path: {}".format(absolutePath))


#CSV files: comma separated value
def read_csv():
    fileName = input("Enter CSV file name: ")
    file = open(fileName)
    content = csv.reader(file)

    for row in content:
        name, country, sex = row
        print("Name: {}, Country: {}, Sex: {}".format(name, country, sex))

    file.close()

def read_csv_disctionary():
    fileName = input("Enter file name: ")

    with open(fileName) as file:
        reader = csv.DictReader(file)
        print(reader)

        for row in reader:
            print(row)
            print("{} is located in {}".format(row["City"],row["Country"]))

def create_csv_dictionary():
    countries = [{"Name": "Estonia", "Capital": "Tallin", "Continent": "Europe"},
        {"Name": "Peru", "Capital": "Lima", "Continent": "America"},
        {"Name": "Austria", "Capital": "Vienna", "Continent": "Europe"},
        {"Name": "Japan", "Capital": "Tokyo", "Continent": "Asia"}]
    keys = ["Name", "Capital", "Continent"]

    with open("list_countries.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(countries)

def write_csv_dictionary():

    return True

#open_file_1()
#open_file_2()
#read_many_files()
#write_file()
#remove_file()
#rename_file()
#get_file_data()

#read_csv()
#write_file()
#read_csv_disctionary()
create_csv_dictionary()
