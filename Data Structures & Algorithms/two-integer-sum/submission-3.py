class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the idea is we take a empty dict and we traverse through each element find their diff from target and check whether diff in dict if diff in dict we return indices of current element and also repsective elemenet else we add it into the list
        dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict:
                return [dict[comp],i]    
            else:
                dict[nums[i]]= i
        return [] 