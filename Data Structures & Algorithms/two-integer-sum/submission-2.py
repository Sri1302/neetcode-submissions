class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute-force solution, for every element , traverse through the next elements of the array.
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        # return []   
        # the optimal solution would be for every element calculate the complement, if complement exists return i,dict[complement] or put the elements into dict.
        dict = {}
        for i in range(len(nums)):
            #calculate the complement
            complement = target - nums[i]
            if complement in dict:
                return [dict[complement],i]
            else:
                dict[nums[i]]=i
        return []