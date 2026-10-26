import numpy as np
import pandas as pd
n=int(input())
students=[]
marks=[]
for i in range(n):
  students.append(input())
  marks.append(int(input()))
a=np.array(marks)
print(np.mean(a))
print(np.median(a))
print(np.max(a))
print(np.min(a))
dp=pd.DataFrame({'Name':students,'marks':marks})
print(dp[dp['marks']>80])