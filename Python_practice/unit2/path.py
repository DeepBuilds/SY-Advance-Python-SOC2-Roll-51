
"""
10. Unique Paths Problem
---------------------------
Determine the number of unique paths from the top-left corner to
the bottom-right corner of a grid, moving only right or down.
 
Approach: Dynamic Programming
    dp[i][j] = number of unique paths to reach cell (i, j)
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    First row and first column are all 1 (only one way to reach them).
"""
 
 
def unique_paths(rows, cols):
    dp = [[1] * cols for _ in range(rows)]
 
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
 
    return dp[rows - 1][cols - 1]
 
 
def main():
    rows = int(input("Enter the number of rows: ").strip())
    cols = int(input("Enter the number of columns: ").strip())
 
    result = unique_paths(rows, cols)
    print(f"Total number of unique paths: {result}")
 