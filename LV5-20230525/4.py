import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from sklearn.cluster import KMeans

# Učitaj sliku
img = image.imread("example.png")

# Prikazi sliku
plt.figure()
plt.title('Originalna slika')
plt.imshow(img)
plt.axis('off')
plt.show()

# Pretvori sliku u vektor
h, w, d = img.shape
img_vector = img.reshape(h * w, d)

# Primijeni K-means na vektor (sliku)
num_clusters = 4  # Broj klastera
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(img_vector)

# Zamijeni boje svakog piksela s najbližim centrom
compressed_img_vector = kmeans.cluster_centers_[kmeans.labels_]
compressed_img = compressed_img_vector.reshape(h, w, d)

# Prikazi dobivenu aproksimaciju (sliku)
plt.figure()
plt.title('Kvantizirana slika sa {} klastera'.format(num_clusters))
plt.imshow(compressed_img)
plt.axis('off')
plt.show()