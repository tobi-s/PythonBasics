import glob
import os

os.chdir("/tmp/")

for file in glob.glob("*.*"):
    print file

print os.getcwd()