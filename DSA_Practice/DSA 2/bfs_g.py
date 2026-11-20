from collections import deque
n=int(input())
m=int(input())
graph=[[] for i in range(n)]
for i in range(m):
  u,v=map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
start=int(input())
visit=[False]*n
queue=deque([start])
visit[start]=True
result=[]
while queue:
  v=queue.popleft()
  result.append(v)
  for i in graph[v]:
    if not visit[i]:
      visit[i]=True
      queue.append(i)
print("BFS :-")
print(*result)