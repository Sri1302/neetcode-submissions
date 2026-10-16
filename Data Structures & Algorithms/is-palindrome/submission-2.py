class Solution:
    def isPalindrome(self, s: str) -> bool:
        # the intution is start using the two pointers
        l,r = 0, len(s)-1
        
        # the condition until we need traverse through the string is left should be behind right
        while l<r:
            # the main condition is strings at postion l and r is alphanumberic 
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            # if postion of string at l and r is not equal we will return False
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1,r-1
        return True
        