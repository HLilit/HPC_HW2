import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor


def main():
        executor = ThreadPoolExecutor(len(os.listdir(sys.argv[1])))
        executor.submit(shutil.copytree(sys.argv[1], sys.argv[2]))

# sys.argv[1]-absolute path to source directory given as a command line arg
# sys.argv[2]-absolute path to dest directory given as a command line arg

if __name__ == "__main__":
        main()
