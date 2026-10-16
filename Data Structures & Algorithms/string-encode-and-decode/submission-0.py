class Solution:

    def encode(self, strs: List[str]) -> str:
        # the idea of this problem is to encode list of string into a string and decode back the string to original list of string
        # the intution for encoding the strings is , if we simply concatenate the string,while decoding how do we split it, and the best approach would be add a delimiter at end of the string , so that we can differentiate both of them, but what if we string itself contains a that special symbol so it better to join the string with len and delimiter and actul string so while decodeing we check the len and consider it while decoding
        res = ""
        for w in strs:
            res+= str(len(w))+"#"+w
        return res

    def decode(self, s: str) -> List[str]:
        # while encoded this way len(str)+"symbol to seperate len with the actual string "+ actual string
        # the intution is start with traversing the string and track the delimiter with a varible if found add to the resulting array and then increment the outer loop with the same.
        ans, i = [], 0
        while i< len(s):
            # we create a new variable which will track the delimiter
            j = i
            while s[j] != '#':
                j+=1
            #if found the delimiter we got the len
            length = int(s[i:j])
            # and we add the string
            ans.append(s[j+1:j+length+1])
            i=j+length+1
        return ans
