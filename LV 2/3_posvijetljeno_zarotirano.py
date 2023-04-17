import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")
img2 = img[:,:,0].copy()
h,v = img2.shape


for i in range (0,h):
    for j in range(0,v):
        img2[i][j] *= 10
        if img2[i][j] > 1:
          img2[i][j] = 1
       

img_rot = np.zeros((v,h))
for i in range (0,h):
    img_rot[:,h-1-i] = img2[i,:]

   # img_rot = np.zeros((h,v))
#for i in range (0,h):
    #img_rot[h-1-i,:] = img2[i,:]
    #kod za mirroranje

img_r=img2[::5,::5]
plt.figure()
#plt.figure()
plt.imshow(img_rot, cmap="gray")
#plt.imshow(img_r, cmap="gray")
#plt.show()
plt.show()


