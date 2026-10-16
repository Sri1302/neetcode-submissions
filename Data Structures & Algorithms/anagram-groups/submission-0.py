class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # intution is convert every string in the list into freq array of 26,if a string has same, freq group 
        groups = {}
        for word in strs:
            # initialise an array of size 26
            count = [0]*26
            #now traverse through the array and inc the freq at subsquent index
            for char in word:
                count[ord(char)-ord('a')]+=1
            # now we have the freq, but there is  catch a a list cannot be python dictionary key , so we convert it into tuple
            key = tuple(count)
            if key not in groups:
                groups[key]= []
            groups[key].append(word)
        return list(groups.values())
            
        