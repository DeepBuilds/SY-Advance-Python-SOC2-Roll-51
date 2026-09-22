def memo(n,dp):
  if n<=1:
    return n
  if dp[n] != -1:
    return dp[n]
  dp[n]=memo(n-1,dp)+memo(n-2,dp)
  return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(memo(n,dp))