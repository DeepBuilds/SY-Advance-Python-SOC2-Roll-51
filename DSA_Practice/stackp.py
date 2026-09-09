stack=[]
class s:
    def do(self,data):
        stack.append(data)
        return "Done: "+ data
    def undo(self):
        if stack:
            n=stack.pop()
            return "Undone: "+ n
        else:
            return "Empty"
    def report(self):
        if len(stack)!=0:
            return "LAST: "+ stack[-1]
        else:
            return "Empty"
    def actions(self):
        
        if stack :
            return "Actions: "+" ".join(reversed(stack))
        else:
            return "Empty"
c=[]
ss=s()
n=int(input())
for i in range(n):
    op=input().split()
    if op[0]=="DO":
        n=ss.do(op[1])
        c.append(n)
    elif op[0]=="UNDO":
        c.append(ss.undo())
    elif op[0]=="LAST":
        c.append(ss.report())
    elif op[0]=="ACTIONS":
        c.append(ss.actions())
for line in c:
     print(line)


    