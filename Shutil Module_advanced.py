import shutil
import os

source = r"E:\Naufil\Python"
destination = r"E:\Naufil\Course 2 Practice and Exercises\CSV Files"


for file in os.listdir(source):
    name, ext = os.path.splitext(file)
    if ext == 'csv':
        source_file = os.path.join(source, file)
        destination_file = os.path.join(destination, file)
        shutil.move(source_file, destination_file)
    else:
        continue

