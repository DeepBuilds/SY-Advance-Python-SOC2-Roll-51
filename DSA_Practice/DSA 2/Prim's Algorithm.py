n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [False] * n
visited[0] = True

mst = []
total = 0

for _ in range(n - 1):
    minimum = float('inf')
    selected = -1
    x = -1

    for i in range(n):
        if visited[i]:
            for v, w in graph[i]:
                if not visited[v] and w < minimum:
                    minimum = w
                    selected = v
                    x = i

    if selected == -1:
        break

    visited[selected] = True
    mst.append((x, selected, minimum))
    total += minimum

for u, v, w in mst:
    print(u, v, w)

print("Total weight:", total)