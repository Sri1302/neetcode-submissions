class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute-force solution, for every element , traverse through the next elements of the array.
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []       