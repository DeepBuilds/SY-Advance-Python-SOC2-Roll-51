'''1.Stack - Library Book Return Management. Implement a stack to manage returned books
with Push (Return Book), Pop (Arrange Book), Peck (Top Book), and Display operations.
these r quetions for my dsa exam give me a code and also explain its working'''
max_size=5
class Stack_lib:
    def __init__(self):
        self.stack = []
    def return_book(self,title):
      
      if len(self.stack) >= max_size:
        print("Stack is full")
        return
      self.stack.append(title)
      print("Append  successful.")
    def arrange(self):
      if len(self.stack) == 0:
        print("stack is empty")
        return
      title=self.stack.pop()
      print(f"{title} popped")
    def peck(self):
      if not self.stack:
        print("Stack is empty")
        return
      print(f"Top book is {self.stack[-1]}")
    def display(self):
      if len(self.stack) == 0:
        print("Stack is empty")
        return
      print("Books in stack r:")
      for book in reversed(self.stack):
        print(book)
def main():
  lib=Stack_lib()
  while True:
    print("\n1.push\n2.pop\n3.peck\n4.disply\n5.Exit")
    choice= int(input("Enter your choice:-"))
    if choice ==1:
      title=input("Enter title of book")
      lib.return_book(title)
    elif choice==2:
      lib.arrange()
    elif choice==3:
      lib.peck()
    elif choice==4:
      lib.display()
    elif choice==5:
      print("Exiting")
      break
    else:
      print("Enter a valid choice")
if __name__=="__main__":
    main()
        
          
      