#!/usr/bin/python 
from sys import argv
from sklearn import metrics
real = open(argv[1]).readlines()
perdict = open(argv[2]).readlines()
rdata = [eval(i) for i in real]
pdata = [eval(i) for i in perdict]
print metrics.classification_report(rdata, pdata)
