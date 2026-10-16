class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the intution is use two pointers
        l,r = 0,len(numbers)-1
        # we need to traverse through the array until left pointer is behind right pointer
        while l<r:
            sum = numbers[l]+numbers[r]
            if sum > target:
                r-=1
            elif sum < target:
                l+=1
            else:
                # as array is indexed from 1
                return [l+1,r+1]
        return []