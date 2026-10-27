class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the idea is to convert each string into freq array and group them based on frequency
        groups = {}
        for word in strs:
            count = [0] *26
            #now we calculate the freq of each char in each word
            for char in word:
                count[ord(char)-ord('a')]+=1
            #now we have freqs of characters in each word
            #but python dict key cant be list , so we convert freq to tuple
            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())