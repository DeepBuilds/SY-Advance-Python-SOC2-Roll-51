def knapsack(weight,values,capacity):
  n=len(weight)
  dp=[[0]*(capacity+1) for i in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,capacity+1):
      if weight[i-1]<=j:
        dp[i][j]=max(values[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])
      else:
        dp[i][j]=dp[i-1][j]
  return dp[n][capacity]
w=list(map(int,input().split(',')))
v=list(map(int,input().split(',')))
cap=int(input())
print(knapsack(w,v,cap))