class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        res = []
        for num in nums:
            hmap[num] += 1
        sortedDict = dict(sorted(hmap.items(), key=lambda item:item[1], reverse=True))    
        for key,val in sortedDict.items():
            if len(res)==k:
                break
            res.append(key)  
        return res        
        