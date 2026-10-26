class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the we need to check length of both strings
        if len(s) != len(t):
            return False
        count = [0]*26
        # we need to array to count the occurances of char in a string and increment it and decrement it for other string
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
        for freq in count:
            if freq!=0:
                return False
        return True