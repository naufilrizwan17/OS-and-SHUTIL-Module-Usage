import os

#This function is used to change the directory
os.chdir(f"E:/Naufil/Course 2 Practice and Exercises")

cwd = os.getcwd()

print("The new directory of this file is: ", cwd)

path = r"E:\Naufil\Course 2 Practice and Exercises"
#This function generates a list of all files in the given directory
dir_list = os.listdir(path)

#Displays a list of all files
print("The list of files in this directory are: ", dir_list)

#Displays the name of the operating system
print(os.name)

source = r"E:\Naufil\Course 2 Practice and Exercises\lab_issu.png"
destination = r"E:\Naufil\Course 2 Practice and Exercises\lab_issue.png"

print("The file has been renamed successfully!")

os.remove("File Writing.py")



