#!/usr/bin/python
import numpy as np
from sys import argv
from sklearn import tree
__author__ = 'TaQini'

if len(argv) != 5:
	print 'usage: '
	print ' $ ./fit.py training_feature training_label predict_fecture predict_label'
	print 'example: '
	print ' $ ./fit.py training.feature training.label X.feature X.label'
	exit(0)

feature_file = open(argv[1],'ro')
label_file = open(argv[2],'ro')

X = np.array([eval(item) for item in feature_file.readlines()])
Y = np.array([eval(item) for item in label_file.readlines()])

feature_file.close()
label_file.close()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

predict_file = open(argv[3],'ro')
predict_lable = open(argv[4],'w+')

pX = np.array([eval(item) for item in predict_file.readlines()])
predict_file.close()

pY = clf.predict(pX)
for i in pY:
    predict_lable.write(str(i)+'\n')
predict_lable.close()
