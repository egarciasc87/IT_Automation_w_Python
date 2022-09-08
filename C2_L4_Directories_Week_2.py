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

def get_working_directory():
    directory = os.getcwd()
    return directory

workingDirectory = get_working_directory()
print("Working directory:", workingDirectory)
#create_directory()
#create_directory()
#remove_directory()
