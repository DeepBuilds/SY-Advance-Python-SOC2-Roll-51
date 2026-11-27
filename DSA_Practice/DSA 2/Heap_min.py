def heapify(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def heap_sort(arr):
    n = len(arr)

    # Build Min Heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


n = int(input())
arr = list(map(int, input().split()))

heap_sort(arr)
print(*arr)