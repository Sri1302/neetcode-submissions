class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the intution is use the two points
        #check whether the elments at left and right position adds up to target if yes return left and right indices values
        l,r = 0, len(numbers)-1
        # we need to traverse through the array until left is behind right
        while l<r:
            if numbers[l]+numbers[r]> target:
                r-=1
            elif numbers[l]+numbers[r] < target:
                l+=1
            else:
                return [l+1,r+1]
        return []
        
        