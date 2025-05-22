# os : operating system

import os

# current wd
pwd = os.getcwd()
print("PWD :",pwd)

# change dir
cd = os.chdir("Exe5_fileH")
print("CD :",os.getcwd())

# list dir & files
ls = os.listdir()
print(ls)

# mkdir
newdir = os.mkdir("demo_folder")

# remove : rm : file delete
rm = os.remove("file.txt")

# rm dir
rmd = os.rmdir("demo_folder")