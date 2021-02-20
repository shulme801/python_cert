#!/usr/bin/env python3

import sys
import os
import re

def count_the_bard(args):
    
    if (len(args) == 0):
        print("You have to supply args to this function")
        return False

    cwd = args[0]
    # if user didn't give us a current working directory to search, use the directory where we are at
    if ((cwd == "") or  (not os.path.isdir(cwd))):
        cwd = os.getcwd()

    file_list = []

    for root, dirs, files in os.walk(cwd,topdown=True):
        files = [f for f in files if ((not f[0] == ''.'') and ())
        for file in files:
            #append the file name to the list
            file_list.append(os.path.join(root,file))
    # print out all the file names
    for name in file_list:
        print(name)

print(count_the_bard(sys.argv[1:]))

'''
# directory_containing_files = "/Users/imtiazahmad/PycharmProjects/Assignments/Section_06/project_files" #sys.argv[1]
# words_to_aggregate = ["hello", "Peter", "computer"] #sys.argv[2:]
directory_containing_files = sys.argv[1]
words_to_aggregate = sys.argv[2:]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

words_and_counts = {}

for word in words_to_aggregate:
    count = 0
    for path, folder_names, file_names in os.walk(directory_containing_files):
        for file_name in file_names:
            file = os.path.join(path, file_name)
            with open(file, "r") as a_file:
                for line in a_file:
                    if re.search(word, line):
                        word_list = re.findall(word, line)
                        count += len(word_list)

    words_and_counts[word] = count



print(words_and_counts)
'''