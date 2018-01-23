#!/usr/bin/python
import numpy as np
from sys import argv
from sklearn import tree
__author__ = 'TaQini'

if len(argv) != 5:
	print 'usage: '
	print ' $ ./fit.py training_feature training_label predict_fecture predict_label '
	print 'example: '
	print ' $ ./fit.py ALL.feature ALL.label X.feature X.label'
feature_file = open(argv[1],'ro')
label_file = open(argv[2],'ro')

X = np.array([eval(item)[1:] for item in feature_file.readlines()])
Y = np.array([eval(item) for item in label_file.readlines()])

feature_file.close()
label_file.close()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

predict_file = open(argv[3],'ro')
# real_label = open(argv[4],'ro')
predict_lable = open(argv[4],'w+')

pX = np.array([eval(item)[1:] for item in predict_file.readlines()])
#rY = np.array([eval(item) for item in real_label.readlines()])

predict_file.close()
#real_label.close()

pY = clf.predict(pX)
for i in pY:
	predict_lable.write(str(i)+'\n')

predict_lable.close()

#cnt = 0
#for i in range(len(pY)):
#	if rY[i] == pY[i]:
#		cnt += 1
#print 'rate: '+str(cnt*100.0/len(Y))+'%'

