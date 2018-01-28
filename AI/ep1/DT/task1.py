#!/usr/bin/python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
__author__ = 'TaQini'

# del item including "NA"
# f = open('./seattleWeather_1948-2017.csv','ro')
# f2 = open('./dataset.csv','w+')
# f2.writelines([i for i in f.readlines() if 'NA' not in i])
# f.close()
# f2.close()

# read dataset
data = pd.read_csv('./dataset.csv')

# add month and day feature
data['MONTH'] = [int(i[5:7]) for i in data.DATE]
data['DAY'] = [int(i[8:10]) for i in data.DATE]
# transform rain as label (1-True, 0-False)
data['LABEL'] = [1 if i==True else 0 for i in data.RAIN]

feature = data.loc[:, ['MONTH','DAY','TMAX','TMIN']]
label = data.loc[:,['LABEL']]

# split data to training_set and test_set
X_train, X_test, Y_train, Y_test = train_test_split(feature, label)

# use DT clf to fit training set
clf = DecisionTreeClassifier(min_samples_leaf=30)
clf = clf.fit(X_train, Y_train)

# predict label
Y_pred = clf.predict(X_test) 

# report
print classification_report(Y_test, Y_pred)
