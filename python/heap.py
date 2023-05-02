import heapq


# Min heap
l = [9, 2, 3, 1, 5, 8, 6]
heapq.heapify(l)
heapq.heappush(l, -1)

while l:
    popped = heapq.heappop(l)
