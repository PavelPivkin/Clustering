from data import readData, writeData, data_list
from sklearn.cluster import KMeans
import numpy as np

def Cluster ():
    #initialaizing data_list
    readData()
    X = np.array(data_list)
    kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

    A_cluster = []
    B_cluster = []
    for x, i in zip(X, kmeans.labels_):
        if (i == 0):
            A_cluster.append(x)
        else:
            B_cluster.append(x)
    writeData(A_cluster, "A_cluster.txt")
    writeData(B_cluster, "B_cluster.txt")
    print "A cluster length = " + str(len(A_cluster))
    print "B cluster length = " + str(len(B_cluster))



Cluster()
