#!/usr/bin/python
#for X,Y,Z
from sys import argv
__author__ = 'TaQini'

if len(argv) != 2:
	print 'usage: '
	print ' $ ./sample_without_label.py <feature_file>'
	print 'example: '
	print ' $ ./sample_without_label.py X.feature'
	exit(0)

feature_file  = open(argv[1],'r')
sample_file = open(argv[1]+'.sample','w+')

# read data
data = feature_file.readlines()
feature_file.close()

# del all item having '?'
result = []
for item in data:
	if '?' not in item:
		result.append(item)

sample_file.writelines(result)
sample_file.close()
