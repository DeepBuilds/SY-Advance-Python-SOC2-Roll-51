def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1) #float('inf') 'inf' is string which is used to represent infinity in Python. It is a special floating-point value that is greater than any other number. In this context, it is used to initialize the dp array with a value that represents an unreachable state, indicating that the amount cannot be formed with the given coins initially.
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


coins = list(map(int, input("Enter coin denominations: ").split()))#splits the input string into a list of strings, converts each string to an integer using map(int, ...), and then creates a list from the resulting map object. This allows the user to input multiple coin denominations separated by spaces, which are then stored as integers in the coins list.
amount = int(input("Enter target amount: "))

result = min_coins(coins, amount)

if result == -1:
    print("Amount cannot be formed")
else:
    print("Minimum number of coins:", result)