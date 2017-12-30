# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 19:52:50 2017

@author: Mark
"""
import pandas as pd
import numpy as np
import os

from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm

#np.set_printoptions(threshold=np.inf)

root_path = "C:/Users/Mark/Dropbox/RodentDataAnalytics-Bees Experiment/Australia Experiment/"

segment_lengths    = [50,100,150,200,250,300]
range_nclusters = range(2,11)

#for testing purposes
segment_lengths = [200]
range_nclusters = range(2,10)

df_features = pd.read_csv(os.path.join(root_path, "Data/length" + str(segment_lengths[0]) + "/segment_features.csv"))
df_xys      = pd.read_csv(os.path.join(root_path, "Data/length" + str(segment_lengths[0]) + "/segment_xys.csv"))

numpy_features = df_features.iloc[:,4:12].values
#fit kmeans
features_scaled = preprocessing.scale(numpy_features)

for n_clusters in range_nclusters:
    # Create a subplot with 1 row and 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # The 1st subplot is the silhouette plot
    # The silhouette coefficient can range from -1, 1 but in this example all
    # lie within [-0.1, 1]
    ax1.set_xlim([-0.1, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette
    # plots of individual clusters, to demarcate them clearly.
    ax1.set_ylim([0, len(features_scaled) + (n_clusters + 1) * 10])
    
    clusterer = KMeans(n_clusters = n_clusters, random_state = 0, max_iter = 1000)
    cluster_labels = clusterer.fit_predict(features_scaled)
    
    #perform voting
    
    
    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(features_scaled, cluster_labels)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)
    
    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(features_scaled, cluster_labels)
    
    y_lower = 10
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values = \
            sample_silhouette_values[cluster_labels == i]
    
        ith_cluster_silhouette_values.sort()
    
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i
    
        color = cm.spectral(float(i) / n_clusters)
        ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)
    
        # Label the silhouette plots with their cluster numbers at the middle
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
    
        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples
    
    ax1.set_title("The silhouette plot for the various clusters.")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")
    
    # The vertical line for average silhouette score of all the values
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
    
    ax1.set_yticks([])  # Clear the yaxis labels / ticks
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
    
    # 2nd Plot showing the actual clusters formed
    colors = cm.spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(features_scaled[:, 0], features_scaled[:, 1], marker='.', s=30, lw=0, alpha=0.7,
                c=colors, edgecolor='k')
    
    # Labeling the clusters
    centers = clusterer.cluster_centers_
    # Draw white circles at cluster centers
    ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
                c="white", alpha=1, s=200, edgecolor='k')
    
    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
                    s=50, edgecolor='k')
    
    ax2.set_title("The visualization of the clustered data.")
    ax2.set_xlabel("Feature space for the 1st feature")
    ax2.set_ylabel("Feature space for the 2nd feature")
    
    plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                  "with n_clusters = %d" % n_clusters),
                 fontsize=14, fontweight='bold')
    
    plt.show()

#perform voting for each x,y coordinate's cluster membership


#for each new segment calculate the features


#calculate the silhouette score





#select a length of segment
#for iseg_length in segment_lengths:
#  
#  #load data
#  #list.files(here("..", "Data", str_c("length", iseg_length)))
#  df = pd.read_csv(os.path.join(root_path, "Data/"))
#  
#  #select how many clusters
#  for(inum_clusters in number_of_clusters){
#    

#    
#    
#  }
#
#}
#repeat the above and determine the length of segment and number of clusters with the optimum silhouette score
