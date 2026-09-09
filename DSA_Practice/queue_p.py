no=int(input())
queue=[]

for i in range(no):
  op=input().split()
  if  op[0] == "ARRIVE":
    n=op[1]
    queue.append(n)
    print("ARRIVED: ",n)
  elif op[0] == "SERVE":
    if len(queue)==0:
      print("not worth")
    else:
      n=queue.pop(0)
      print("SERVE: ",n)
  elif op[0] == "QUEUE":
    if len(queue)==0:
      print("empty")
    else:
      print("Waiting: "," ".join(queue))
  
  