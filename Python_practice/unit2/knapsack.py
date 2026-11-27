weight = [1, 3, 4, 5]
value = [1, 4, 5, 7]
capacity = 7

items = len(weight)
dp = [[0] * (capacity + 1) for _ in range(items + 1)]

for item in range(1, items + 1):
    for bag in range(1, capacity + 1):

        if weight[item-1] <= bag:
            dp[item][bag] = max(
                value[item-1] + dp[item-1][bag-weight[item-1]],
                dp[item-1][bag]
            )
        else:
            dp[item][bag] = dp[item-1][bag]

print(dp[items][capacity])