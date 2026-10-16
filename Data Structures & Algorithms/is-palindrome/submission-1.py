class Solution:
    def isPalindrome(self, s: str) -> bool:
        #the intution is create a new str with only alphanumeric values
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr+=c.lower()
        return newStr == newStr[::-1]
        