n, m = map(int, input().split())

edges = []

for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    xroot = find(x)
    yroot = find(y)

    if xroot != yroot:
        parent[xroot] = yroot
        return True
    return False

mst = []
total = 0

for w, u, v in edges:
    if union(u, v):
        mst.append((u, v, w))
        total += w

    if len(mst) == n - 1:
        break

for u, v, w in mst:
    print(u, v, w)

print("Total weight:", total)
