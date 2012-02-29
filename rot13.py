#!/usr/bin/env python
import fileinput
import string

table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

for line in fileinput.input():
    line = line.rstrip()
    print string.translate(line, table)
