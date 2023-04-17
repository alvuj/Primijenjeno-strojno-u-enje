import numpy as np
import matplotlib.pyplot as plt
b = np.array([[3,7,1],[4,5,6]])
x = np.array([1,2,3,3,1])
y= np.array([1,2,2,1,1])
plt.plot(x, y, 'b', linewidth=3, marker=".", markersize=10)
plt.axis([0,4,0,4])
plt.xlabel('x')
plt.ylabel('vrijednosti funkcije')
plt.title('sinus funkcija')
plt.show()
