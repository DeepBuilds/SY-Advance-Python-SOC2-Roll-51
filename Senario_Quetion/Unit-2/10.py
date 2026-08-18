#10. Unique Paths Problem
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

dp = [[0] * cols for _ in range(rows)]

# First row and first column have only one path
for i in range(rows):
    dp[i][0] = 1

for j in range(cols):
    dp[0][j] = 1

# Calculate remaining paths
for i in range(1, rows):
    for j in range(1, cols):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print("Total number of unique paths:", dp[rows-1][cols-1])
'''
Enter number of rows: 5
Enter number of columns: 6
Total number of unique paths: 126

'''