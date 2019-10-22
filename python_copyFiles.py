import os
import shutil
import sys


def main():
    shutil.copytree(sys.argv[1], sys.argv[2])

# sys.argv[1]-absolute path to source directory given as a command line arg
# sys.argv[2]-absolute path to dest directory given as a command line arg

if __name__ == "__main__":
    main()
