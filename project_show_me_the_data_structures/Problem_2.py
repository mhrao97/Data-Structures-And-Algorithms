# Problem 2 - File Recursion

import sys
sys.path.append("c:/Users/M/Anaconda3/Lib/site-packages/")

# Your work here

# function to check if a file exists
def file_exists(path):
    return os.path.exists(path)


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    list_of_paths = []
    sub_dir_path = []

    for i_file in os.listdir(path):
        i_file = os.path.join(path, i_file)

        if os.path.isfile(i_file) == True:
            if i_file.endswith(suffix) == True:
                list_of_paths.append(i_file)
        elif os.path.isdir(i_file) == True:
            sub_dir_path = find_files(suffix, i_file)

        for sub_dir in sub_dir_path:
            list_of_paths.append(sub_dir)

    return list_of_paths

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
# print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))              # prints True or False depending on if the file exists

# Does the file end with .py?
print ("./ex.py".endswith(".py"))              # prints True or False depending on if the file exists

test_results = find_files(".c", "./testdir")
print(test_results)                            # prints list of files in testdir folder

test_results2 = find_files(".h", "./")
print(test_results2)                           # prints files with .h extension

test_results3 = find_files(".txt", "./")
print(test_results3)                           # prints files with .txt extension
