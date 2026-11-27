"""top down"""
def knapsack(weight, value, capacity, items, dp):

    if items == 0 or capacity == 0:
        return 0

    if dp[items][capacity] != -1:
        return dp[items][capacity]

    if weight[items-1] <= capacity:
        dp[items][capacity] = max(
            value[items-1] + knapsack(weight, value, capacity-weight[items-1], items-1, dp),
            knapsack(weight, value, capacity, items-1, dp)
        )
    else:
        dp[items][capacity] = knapsack(weight, value, capacity, items-1, dp)

    return dp[items][capacity]


weight = [1, 3, 4, 5]
value = [1, 4, 5, 7]
capacity = 7
items = len(weight)

dp = [[-1] * (capacity+1) for _ in range(items+1)]

print(knapsack(weight, value, capacity, items, dp))