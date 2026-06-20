class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k
        maxElem = max(nums[start:k])
        result = [maxElem]
        while(end<len(nums)):
            if nums[end]>maxElem:
                maxElem = nums[end]
            elif maxElem == nums[start]:
                maxElem = max(nums[start+1:end+1])
            result.append(maxElem)
            end+=1
            start+=1    
        return result    


        