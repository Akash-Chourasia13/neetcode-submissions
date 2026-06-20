class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        res = [0,0]
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hmap:
                hmap[nums[i]] = []  
                hmap[nums[i]].append(i) 
            else:    
                res = [hmap[diff][0],i]
        return res        

        