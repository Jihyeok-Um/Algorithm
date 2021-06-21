import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    count = 0
    while (heap[0] < K and len(heap) >= 2):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        result = a + b * 2
        heapq.heappush(heap, result)
        count += 1

    if (heap[0] < K):
        return -1
    return count 
