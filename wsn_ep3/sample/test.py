#!/usr/bin/python
from subprocess import *

training_set = 'ABCDE' 
test_set = 'ABCDE'

for i in training_set:
	for j in test_set:
		if i!=j:
			pf = Popen(('./fit.py '+i+'.feature.sample '+i+'.label.sample '+j+'.feature.sample '+j+'.label').split(),stdout=PIPE)
			pf.communicate()
			pe = Popen(('./evaluate.py '+j+'.label.sample '+j+'.label').split(),stdout=PIPE)
			print i,j,pe.communicate()[0],
