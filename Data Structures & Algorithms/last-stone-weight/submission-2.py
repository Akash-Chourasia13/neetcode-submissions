import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            h1 = -heapq.heappop(heap)
            h2 = -heapq.heappop(heap)
            if abs(h1-h2) != 0:
                heapq.heappush(heap,-abs(h1-h2))
        return -heap[0] if heap else 0       

        