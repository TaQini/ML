#!/usr/bin/python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
__author__ = 'TaQini'

# open data set file 
feature_file = open('./training.feature','ro')
label_file = open('./training.label','ro')

# read file
X = np.array([eval(item) for item in feature_file.readlines()])
Y = np.array([eval(item) for item in label_file.readlines()])

# close file 
feature_file.close()
label_file.close()

# split data to training_set and test_set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

# use DT clf to fit training set
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)

# predict label
Y_pred = clf.predict(X_test)

# report
print classification_report(Y_test, Y_pred)
