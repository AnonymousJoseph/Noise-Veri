from sklearn.cluster import OPTICS
import numpy as np

# Gürültü veri ile birlikte verinin oluşturulması
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [100, 101], [101, 102], [102, 103]])

# OPTICS modelinin oluşturulması
clustering = OPTICS(min_samples=2, xi=.05, min_cluster_size=.05).fit(X)

# Kümelerin çıktısını almak
print(clustering.labels_)
