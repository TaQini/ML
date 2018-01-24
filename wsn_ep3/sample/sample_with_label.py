#!/usr/bin/python
#for A,B,C,D,E
from sys import argv
__author__ = 'TaQini'

if len(argv) != 3:
	print 'usage: '
	print ' $ ./sample_with_label.py <feature_file> <label_file>'
	print 'example: '
	print ' $ ./sample_with_label.py A.feature A.label'
	exit(0)

feature_file  = open(argv[1],'ro')
label_file = open(argv[2],'ro')
feature_sample_file = open(argv[1]+'.sample','w+')
label_sample_file = open(argv[2]+'.sample','w+')

# read data
fdata = feature_file.readlines()
ldata = label_file.readlines()
feature_file.close()
label_file.close()

# del all item having '?'
feature = []
label = []
for item in range(len(fdata)):
	if '?' not in fdata[item]:
		feature.append(fdata[item])
		label.append(ldata[item])

feature_sample_file.writelines(feature)
feature_sample_file.close()

label_sample_file.writelines(label)
label_sample_file.close()
