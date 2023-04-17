import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)
x = data[:,0]
y = data[:,3]
s = data[:,5]
cyl = data[:,1]
print(x)
print(data.shape)
plt.scatter(x, y,s=s*10)
plt.xlabel("mpg")
plt.ylabel("hp")
plt.show()


min = np.min(x)
max = np.max(x)
mean = np.mean(x)
print ("min max")
for i in cyl:
    if i == 6:
        print("min", min)
        print("max", max)
        print("mean", mean)
