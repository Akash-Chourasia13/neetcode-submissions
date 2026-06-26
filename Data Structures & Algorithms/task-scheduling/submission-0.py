import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = {}
        for task in tasks:
            if task in hmap:
                hmap[task] += 1
            else:
                hmap[task] = 1

        total = 0
        heap = [-v for v in hmap.values()]
        heapq.heapify(heap) 
        while heap:
            temp = []
            for cycle in range(n+1):
                if heap:
                    freq = 1 + heapq.heappop(heap)
                    if freq != 0:
                        temp.append(freq)
                total += 1

                if not heap and not temp:
                    break

            for tmp in temp:
                heapq.heappush(heap,tmp)
        return total            





        