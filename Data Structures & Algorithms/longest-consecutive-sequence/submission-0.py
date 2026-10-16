class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         # we convert the list into set to avoid duplicates
        numsSet = set(nums)
        longest = 0
        # longest tracks the longest sequence so far
        for n in nums:
            # we need to check whether the element is start of sequence.
            if n-1 not in numsSet:
                length = 0
                while n+length in numsSet:
                    length+=1
                longest = max(length, longest)
        return longest
       