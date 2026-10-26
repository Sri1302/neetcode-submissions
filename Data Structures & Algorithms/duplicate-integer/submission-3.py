class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #it is better to use set
        hset = set()
        for num in nums:
            if num in hset:
                return True
            else:
                hset.add(num)
        return False