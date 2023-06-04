import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())
#3 zadaci
print("zadaci")
print(df.count(axis='columns'))
print(df.dtypes)
mtcars_mpg=df.sort_values(by=['selling_price'])
print("najjeftiniji")
print (mtcars_mpg.head(1))
print("NAJSKUPLJI")
print (mtcars_mpg['name'].tail(1))

print("2012 proztvedeniu")
#new_mtcars = mtcars[mtcars.cyl >= 6]
print(df[df.year == 2012].count())

print("Najvise Km")
mtcars_km=df.sort_values(by=['mileage'])

print (mtcars_km[['name','mileage']].head(1))

print("najmanje km")
print (mtcars_km[['name','mileage']].tail(1))
# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

tabcorr = df.corr()
sns.heatmap(df.corr(), annot=True, linewidths=2, cmap= 'coolwarm') 

plt.show()

#3 zadaci
print("zadaci")
print(df.count(axis='name'))
