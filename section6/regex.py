#!/usr/bin/env python3

import re

txt = "sample2.txt"
print(txt)

x = re.search("txt", txt)
print(x)
if (x == True):
    print("Found it")
else:
    print("not found")

