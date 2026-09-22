def path(row,col):
  dp=[[1]*col for i in range(row)]
  for i in range(1,row):
    for j in range(1,col):
      dp[i][j]=dp[i-1][j]+dp[i][j-1]
  return dp[row-1][col-1]
row=int(input())
col=int(input())
print(path(row,col))
