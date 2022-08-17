import os

def create_directory():
    directory = input("Enter new directory:")
    os.mkdir(directory)

def remove_directory():
    directory = input("Enter new directory:")
    os.rmdir(directory)

def chage_working_directory():
    directory = input("Enter new directory:")
    os.chdir(directory)

workingDirectory = os.getcwd()
print("Working directory:", workingDirectory)
#create_directory()
remove_directory()
