class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            #we take the freq of elements where we add it if element in s, and subtract it if element is in t.
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
        # now we have freq in count
        for freq in count:
            if freq!=0:
                return False
        return True
        