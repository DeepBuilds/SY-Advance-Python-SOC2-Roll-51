MAX_SIZE = 5
queue = []

def enqueue(item):
    if len(queue) >= MAX_SIZE:
        print("Queue is full")
    else:
        queue.append(item)
        print(item, "added to queue")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print(queue.pop(0), "removed from queue")

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)


while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item: ")
        enqueue(item)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")