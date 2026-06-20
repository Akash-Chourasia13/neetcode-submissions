class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num]+=1
                if hmap[num]>1:
                    return True

        return False 