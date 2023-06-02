from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=n, random_state=0).fit(data)
labels = kmeans.labels_
centers = kmeans.cluster_centers_