n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

start = int(input())

visited = [False] * n
stack = [start]
result = []

while stack:
    v = stack.pop()

    if not visited[v]:
        visited[v] = True
        result.append(v)

        for i in range(n - 1, -1, -1):
            if graph[v][i] == 1 and not visited[i]:
                stack.append(i)

print("Road Network DFS Traversal:")
print(*result)