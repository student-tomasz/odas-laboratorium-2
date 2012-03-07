#!/usr/bin/env python
import sys, string

def get_stats(filepath):
    stats = {}
    char_count = 0
    for char in string.ascii_lowercase:
        stats[char] = 0
    for line in open(filepath):
        line = line.strip().lower()
        for char in line:
            char_count += 1
            if char in stats:
                stats[char] += 1

    accepted_chars = string.ascii_lowercase
    sorted_chars = sorted(stats)
    result = {}
    for char in sorted_chars:
        if char in accepted_chars:
            result[char] = float(stats[char])/char_count
            # print "%s => %d " % (char, stats[char])
    return result

stats = {}
for lang in ('en', 'la'):
    stats[lang] = get_stats("lorem_ipsum_%s.txt" % lang)
prognosis = {}
for lang in stats:
    prognosis[lang] = 0

def guess_lang():
    curr_stats = get_stats(sys.argv[1])
    for lang in stats:
        for char in curr_stats:
            stat = stats[lang][char]
            if (curr_stats[char] >= stat*0.9) and (curr_stats[char] <= stat*1.1):
                prognosis[lang] += 1
    best_lang = 'en'
    for lang in prognosis:
        if prognosis[best_lang] < prognosis[lang]:
            best_lang = lang
    print best_lang

guess_lang()
