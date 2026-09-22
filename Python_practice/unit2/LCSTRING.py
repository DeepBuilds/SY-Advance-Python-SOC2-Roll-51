def LCS(s1,s2):
  m,n=len(s1),len(s2)
  dp=[[0]*(n+1) for i in range(m+1)]
  max_count=0
  for i in range(m+1):
    for j in range(n+1):
      if s1[i-1]==s2[j-1]:
        dp[i][j]=dp[i-1][j-1]+1
        max_count=max(max_count,dp[i][j])
      else:
        dp[i][j]=0
  return max_count
s1=input()
s2=input()
print(LCS(s1,s2))