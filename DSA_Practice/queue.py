queue=[]
max_s=5
def enq(data):
  if len(queue)!=max_s:
    queue.append(data)
    return f"Done:{data}"
  
def deq():
  if queue:
    data=queue.pop(0)
    
    return f"Deque:{data}"
  else:
    return 'Empty'
def display():
  
  if queue:
    return queue
  else:
    return "empty"
result=[]
n=int(input())
for i in range(n):
  op=input().split()
  if op[0]=='enqueue':
    result.append(enq(op[1]))
  elif op[0]=='dequeue':
    result.append(deq())
  elif op[0]=='display':
    result.append(display())
for i in result :
  print(i)

  
  

      
  
