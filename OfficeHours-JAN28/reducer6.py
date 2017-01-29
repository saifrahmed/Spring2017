#!/usr/bin/python
from __future__ import division
import sys
        
total = 0
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    word, count = line.split()
    count = int(count)
    
    
    if word == "**CountTotals":
        total += count
    else:
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print '%s\t%s\t%s\t%s' % (current_word, current_count, current_count/total,total)
            current_count = count
            current_word = word

    # do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s\t%s\t%s' % (current_word, current_count, current_count/total,total)
      