class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #as the problem does the list contains duplicates we can use set
        hset = set()
        for num in nums:
            if num in hset:
                return True 
            else:
                hset.add(num)
        return False