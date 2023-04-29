print("test")
import os
import random
import shutil
cwd = os.getcwd()
name = "pyPackage" + str(random.randint(1,999))
path = os.path.join(cwd, name)
os.mkdir(path)
folderToCopy = input("Please provide path to folder")
file = open(path + "/LICENSE", "w")
file.close()
file = open(path + "/pyproject.toml", "w")



file.close()

file = open(path + "/README.md", "w")
file.close()


path2 = os.path.join(path, "src/")
os.mkdir(path2)
file = open(path2 + "/__init__.py", "w")
file.close()
if os.path.isdir(folderToCopy) == False:
    print("Not a Directory")
    exit()
filesToCopy = os.listdir(folderToCopy)
for file in filesToCopy:
        shutil.copy(folderToCopy + file, path2 + file)
        print(path2)


