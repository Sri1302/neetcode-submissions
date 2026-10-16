class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force approch would be for every element we need iteratet through all the leements of the array without the number itself
        # arr = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i !=j:
        #             prod = prod*nums[j]
        #     arr.append(prod)
        # return arr
        #the brute force approach when submitted exceede the time-limit
        # now lets think of two array which holds the prefix and postfix of repective values in an array and mutiply them
        postfix = [1] * len(nums)
        prefix = [1] * len(nums)

        # updating the prefix values 
        for i in range(len(nums)):
            if i !=0:
                prefix[i]=prefix[i-1]* nums[i-1]
        
        # updating the postfix values
        for i in range(len(nums)-1,-1,-1):
            if i!=len(nums)-1:
                postfix[i]= postfix[i+1]* nums[i+1]
        
        # mutiply both postfix and prefix arrays
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i]= prefix[i]* postfix[i]
        return result