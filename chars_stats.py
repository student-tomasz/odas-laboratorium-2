#!/usr/bin/env python
import sys, re, string

stats = {}
for line in sys.stdin.readlines():
    line = re.sub(r'\s', '', line)
    line = line.lower()
    for char in line:
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 0

sorted_chars = sorted(stats)
for char in sorted_chars:
    print "%s => %d " % (char, stats[char])
