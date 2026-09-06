'''Singly Linked List -Dynamic Library Catalog. Implement a Singly Linked List with
Insert at beginning, Insert at end, Delete from beginning, and Display operations.'''



class Node:
  def __init__(self,book):
    self.book=book
    self.next=None
class LL:
  def __init__(self):
    self.head=None
  def insert_begin(self, book):
    new_node=Node(book)
    new_node.next= self.head
    self.head=new_node
    print("sucessful")
  def insert_end(self,book):
    new_node = Node(book)
    if self.head is None :
      self.head=new_node
      return
    temp = self.head
    while temp.next is not None:
      temp = temp.next
    temp.next = new_node
  def delete_begin(self):
    if self.head is None:
      print("Empty")
      return
    removed= self.head
    print(removed,"removed")
    self.head =self.head.next
  def display(self):
    if self.head is None:
      print("its empty")
      return
    temp=self.head
    while temp.next is not None:
      print(temp.book,"->",end="")
      temp = temp.next
    print("None")
def main():

    ll=LL()
    while True:
        print("\n1.insert_begin\n2.insert_end\n3.Delete_begining\n4.display\n5exit")
        choice=input("Enter ur choice")
        if choice == "1":
            book=input("book name")
            ll.insert_begin(book)
        elif choice == "2":
            book=input("book name")
            ll.insert_end(book)
        elif choice == "3":
            ll.delete_begin()
        elif choice == "4":
            ll.display()
        elif choice == "5":
            print("Exiting")
            break
        else:
            print("Enter a valid choice.")
if __name__ == "__main__":
    main()
    
      
      
    
      
      