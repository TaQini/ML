#!/usr/bin/python
#list type of labels
from numpy import unique
from sys import argv
__author__ = 'TaQini'

if len(argv) != 2:
	print 'usage: '
	print ' $ label.py <label_file>'
	exit(0)

label_file = open(argv[1],'ro')
data = label_file.readlines()
label = []

for item in data:
	label.append(eval(item[:-1]))

print unique(label)
