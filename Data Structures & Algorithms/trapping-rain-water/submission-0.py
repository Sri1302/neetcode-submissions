class Solution:
    def trap(self, height: List[int]) -> int:
        # the intution is to use two pointers
        l,r = 0, len(height)-1
        # we keep track of 2 variables called maxl and maxr which gonna have maximum heights intially 
        maxl,maxr = height[l],height[r]
        water = 0
        # we traverse through the array until left pointer is behind right pointer
        while l<r:
            if maxl > maxr:
                #if maxl is greater than maxr, we move right pointer
                r-=1
                maxr = max(maxr,height[r])
                water+=maxr-height[r]
            else:
                l+=1
                maxl = max(maxl,height[l])
                water+=maxl-height[l]
        return water

