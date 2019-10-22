import os
import shutil
import sys


def cpy(src, dst):
        shutil.copy(src, dst)

# sys.argv[1] - source directory path as a command line argument
# sys.argv[2] - destination directory path as a command line argument

for filename in os.listdir(sys.argv[1]):
        cpy(sys.argv[1]+'/'+filename, sys.argv[2])
