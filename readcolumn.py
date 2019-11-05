import pandas
import shivfun
df=pandas.read_csv('PRODUCTS.csv')
#print(df['Name'])
nm=list(df['Name'])
print(nm[0])
pr=list(df['Regular price'])
#print(min(pr))
shivfun.Mymax(pr)