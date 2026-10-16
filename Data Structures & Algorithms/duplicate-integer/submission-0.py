class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        # set converts iterable like list into set
        for i in range(len(nums)):
            if nums[i] in hset:
                return True
            else:
                hset.add(nums[i])
        return False