#!/usr/bin/python 
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from itertools import cycle
__author__ = 'TaQini'

# read dataset
data = pd.read_csv('./data_1024.csv',sep='\t')

# get feature
f1 = data['Distance_Feature'].values
f2 = data['Speeding_Feature'].values
X = np.matrix(zip(f1,f2))

# choose k=2 and run kmeans
# kmeans = KMeans(n_clusters=2).fit(X)
# choose k=4 
kmeans = KMeans(n_clusters=4).fit(X)

labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
print("number of estimated clusters : %d" % n_clusters_)

# draw 
plt.figure(1)
plt.clf()
for k, col in zip(range(n_clusters_), cycle('bgmcy')):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(X[my_members, 0], X[my_members, 1], col+'.')
    plt.plot(cluster_center[0], cluster_center[1], '*', markerfacecolor='r', markeredgecolor='k', markersize=20)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
