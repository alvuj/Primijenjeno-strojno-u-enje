import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()
h,v = img.shape

for i in range (0,h):
    for j in range(0,v):
        img[i][j] *= 10
        if img[i][j] > 1:
          img[i][j] = 1


img_rot = np.zeros((v,h))
for i in range (0,h):
    img_rot[:,h-1-i] = img[i,:]


imgzrcalo = np.zeros((v,h))
for i in range (v):
    imgzrcalo[v-1-i,:]= img_rot[i,:]
faktor = 10
img_resized = np.zeros((v//faktor,h//faktor))
for i in range(v):
    for j in range(h):
        
        i_resized = i // faktor
        j_resized = j // faktor
        
        if (i + faktor) % 10 == 0 and (j + faktor) % 10 == 0:
            img_resized[i_resized,j_resized]= imgzrcalo[i,j]


img_second_forth = np.zeros((h,v))
for i in range(h):
    for j in range(v):
        if 240 <= j < 480:
            img_second_forth[i,j]=img[i,j]



plt.figure()
plt.imshow(img_second_forth, cmap="gray")
plt.show()