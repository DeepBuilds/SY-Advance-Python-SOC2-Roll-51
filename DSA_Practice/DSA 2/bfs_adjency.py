#bfs in adjecency lsit
from collections import deque
ver=int(input())
ed=int(input())
graph=[[] for i in range(ver)]
for i in range(ed):
  v,m=map(int,input().split())
  graph[v].append(m)
  graph[m].append(v)
start=int(input())
result=[]
visited=[False]*ver
visited[start]=True
q=deque([start])
while q:
  v=q.popleft()
  result.append(v)
  for i in graph[v]:
    if not visited[i]:
      visited[i]=True
      q.append(i)
print(*result)
      