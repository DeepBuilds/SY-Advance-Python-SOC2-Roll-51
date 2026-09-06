#Without list
def fib_memo(n,dp={}):
  if n<=1:
    return n
  if n in dp:
    return dp[n]
  dp[n]=fib_memo(n-1,dp)+fib_memo(n-2,dp)
  return dp[n]
num=int(input("Enter num:- "))
print("Fib num is :- ",fib_memo(num))
#with list 
def fib_memo_1(n,dp):
  if n<=1:
    return n
  if n != dp:
    return dp[n]
  dp[n]=fib_memo(n-1,dp)+fib_memo(n-2,dp)
  return dp[n]

num1=int(input("Enter num:- "))
dp=[-1]*(num1+1)
print("Fib num is :- ",fib_memo_1(num1,dp))