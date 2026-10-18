class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #sort the array so that we will not endup putting the same triplets
        for i,a in enumerate(nums):
            # if you want to iterarate through both index and value use enumerate
            #as array is sorted same elements will be next to each other, so what we do we check i should be greater than zero and element with previous index value and if found match we skip
            if i>0 and a == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            #we traverse through the arry until left pointer is behind right pointer
            while l<r:
                threeSum = a+ nums[l]+nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    r-=1
                    while nums[r] == nums[r+1] and l<r:
                        r-=1
        return res
                
        