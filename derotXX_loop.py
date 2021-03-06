#!/usr/bin/env python
import fileinput, sys, string

def gcd(a, b):
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b / gcd(a, b))

def derot_loop_count(rot, alphabet_length):
    return int((float(lcm(rot_by, 26))/rot_by) - 1)

rot_by = int(sys.argv[1])

from_chars = string.ascii_uppercase + string.ascii_lowercase
to_chars = ""
alphabet_length = len(from_chars)/2
for half in (0,1):
    offset = half * alphabet_length
    for i in range(offset, offset + alphabet_length):
        to_chars += from_chars[offset + (i+rot_by*derot_loop_count(rot_by, alphabet_length)) % alphabet_length]
# print from_chars
# print to_chars

translate_table = string.maketrans(from_chars, to_chars)

for line in fileinput.input(sys.argv[2:]):
    line = line.strip()
    print line.translate(translate_table)
