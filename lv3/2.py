import pandas as pd
from matplotlib import pyplot as plt
 
# Read CSV into pandas
data = pd.read_csv('mtcars.csv')
data.head()
df = pd.DataFrame(data)
x1 = data[((data.cyl == 4) & (data.cyl == 6) & (data.cyl == 8))]

ax = df.plot.bar(x=x1, y='car', rot=0)
plt.show()
