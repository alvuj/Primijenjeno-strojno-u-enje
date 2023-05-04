import pandas as pd
import numpy as np
mtcars = pd.read_csv('mtcars.csv')
#print(mtcars.sort_values(by=['mpg']))
#1
mtcars_mpg=mtcars.sort_values(by=['mpg'])
print (mtcars_mpg.head(5))

#2

cyl8 = mtcars[mtcars.cyl == 8]
auto3 = cyl8.sort_values(by='mpg').head(3)
print("Tri automobila s 8 cilindara i najmanjom potrošnjom:", cyl8)
#3 Kolika je srednja potrošnja automobila sa 6 cilindara?
new_mtcars = mtcars[mtcars.cyl >= 6]
print("srednja potrsosnja je ", new_mtcars['mpg'].mean())

#4
cars4 = mtcars[(mtcars.cyl == 4) & ((mtcars.wt * 1000 ) >= 2000) & ((mtcars.wt *1000) <= 2200)]
print("srednja potrosnja auta s 4 cilindara i između 2000 i 2200 lbs je : ", cars4['mpg'].mean())

#print(cars4.columns)
print(cars4)
#print(len(cars4))

#5

#print(mtcars['gear'])
mjenjac = mtcars[(mtcars.gear >= 4)]
print(mjenjac)
print(mtcars[['car','am','gear']].value_counts())

#6 6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
print("666666666666")
mjenjac_konji = mtcars[(mtcars.gear >= 4 ) & (mtcars.hp >= 100)]
print(mjenjac_konji)


#7 Kolika je masa svakog automobila u kilogramima?

print("sedmi")
mtcars['wt_kg'] = mtcars['wt'] * 1000 * 0.453592
print(mtcars[['car','wt_kg']])




