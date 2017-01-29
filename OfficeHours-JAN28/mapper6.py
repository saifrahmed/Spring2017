#!/usr/bin/python
from __future__ import division
import math
import sys
import re



for line in sys.stdin:
  line = line.strip()
  for word in re.findall(r'[a-z]+', line.lower()):
   
    print "**CountTotals\t",1
    print word,"\t",1