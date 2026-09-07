def change(coins,amount):
  dp=[0]*(amount+1)
  dp[0]=1
  for coin in coins:
    for i in range(coin,amount+1):
      dp[i]=dp[i]+dp[i-coin]
  return dp[amount]
coins=list(map(int,input("Enter coins :- ").split()))
amount = int(input("Enter amount"))
print(change(coins,amount))