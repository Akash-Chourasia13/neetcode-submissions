class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        maxAmt = 0

        while left < right:
            maxAmt = max(maxAmt, (min(heights[left],heights[right]))*(right-left))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxAmt            

        