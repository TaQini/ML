#!/usr/bin/python 
from sys import argv
real = open(argv[1]).readlines()
perdict = open(argv[2]).readlines()
rdata = [eval(i) for i in real]
pdata = [eval(i) for i in perdict]
cnt = 0
for i in range(len(rdata)):
	if rdata[i] == pdata[i]:
		cnt += 1
print 100.0*cnt/len(rdata)
