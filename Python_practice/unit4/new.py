import pandas as pd
import matplotlib.pyplot as pt
dp=pd.read_csv('sales.csv')

print(dp['Sales'].sum())
print(dp['Sales'].mean())
print(dp[dp['Sales']==dp['Sales'].max()]['Month'])
grpc=dp.groupby('Category')['Sales'].sum()
pt.bar(grpc.index,grpc.values)
pt.show()
grpm=dp.groupby('Month')['Sales'].sum()
pt.plot(grpm.index,grpm.values)
pt.pie(grpc.values,labels=grpc.index,autopct='%1.1f%%')

pt.show()