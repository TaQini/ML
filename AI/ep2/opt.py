#!/usr/bin/python 
# script to find the optimal threshold
import pandas as pd
from sys import argv
if len(argv) != 2:
	print "usage: "
	print "$ ./opt.py log_file"
	exit(0)

log_file = argv[1]
a = 1.5
df = pd.read_csv(log_file, sep=' ').values
best = df[-1][0]
maxt = 0
for i in df:
	if i[0] > best and i[1] > maxt:
		maxt = i[1]
print 'optimal threshold: %d' % int(a * maxt)
