class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the intution is to use two pointers
        l,r = 0,len(heights)-1
        res = 0
        # the condition we use to traverse through the array is left pointer should be behind right pointer
        while l<r:
            area = (r-l)*min(heights[r],heights[l])
            res = max(area,res)
            #how do we shift the pointers
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return res
        