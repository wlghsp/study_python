import numpy as np

np.random.seed(123)
X = np.random.random_sample([5,3]) * 10

import pandas as pd

variables = ['X', 'Y', 'Z']
labels = ['ID_0','ID_1','ID_2','ID_3','ID_4']
df = pd.DataFrame(X, columns=variables,index=labels)
print(df)

from scipy.spatial.distance import pdist, squareform

Y = pdist(df) # df <- X,Y,Z
print(Y)

row_dist = pd.DataFrame(squareform(pdist(df, metric='euclidean')),
                        columns=labels, index=labels)

from scipy.cluster.hierarchy import linkage

row_clusters = linkage(pdist(df, metric='euclidean'), method='complete')

pd.DataFrame(row_clusters, columns=['row label 1','row label 2', 'distance', 'no. of items in clust.'],
             index=['cluster %d' % (i+1) for i in range(row_clusters.shape[0])])

