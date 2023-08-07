import os
import shutil

source = r"E:\Naufil\Course 2 Practice and Exercises"

# Create subdirectories if they don't exist
subdirs = ["CSV Files", "TXT Files", "Pics", "Python Files"]
for subdir in subdirs:
    if not os.path.exists(subdir):
        os.makedirs(subdir)

# Loop through files in the source directory
for file in os.listdir(source):
    name, ext = os.path.splitext(file)
    print(name)
    print(ext)
# Conditions which each check the respective extensions of the file and move it to a specific directory
    if ext == '.csv':
        shutil.move(os.path.join(source, file), os.path.join(source, "CSV Files", file))
        print("This file: {} is a csv file".format(file))
    elif ext == ".txt":
        shutil.move(os.path.join(source, file), os.path.join(source, "TXT Files", file))
        print("This file: {} is a txt file".format(file))
    elif ext == ".jpg" or ext == ".png":
        shutil.move(os.path.join(source, file), os.path.join(source, "Pics", file))
        print("This file: {} is an image/screenshot".format(file))
    elif ext == ".py":
        shutil.move(os.path.join(source, file), os.path.join(source, "Python Files", file))
        print("This file: {} is a python file".format(file))
    else:
        print("This file: {} is not any csv, txt, png, jpg or py file".format(file))

print("File organization complete!")
