class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #intution is first take all the distinct element in the dict with their freqs and then convert it into arr and sort it in descending order and then return the top k elements
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]= 1
        # now we have dictionary with distinct elements and their freqs
        # now the idea use priority queue
        heap = []
        for key in dict:
            freq = dict[key]
            heapq.heappush(heap,(freq,key))
            if len(heap)>k:
                # remve the weakest element with less freq
                heapq.heappop(heap)
        # now our consists of [(2,3),(1,2)]
        # now our heap the contains the arr with highest freqs
        result = []
        for i in range(len(heap)):
            result.append(heap[i][1])
        return result

        # #at this point we have all our elements in the dictionary witht their freqs
        # # convert the dict into arr
        # arr = []
        # for key in dict:
        #     arr.append((key,dict[key]))
        # # now we have a array with all our elements
        # # sort  it in descending order
        # for i in range(len(arr)):
        #     for j in range(i+1,len(arr)):
        #         # compare the freqs
        #         if arr[i][1] < arr[j][1]:
        #             arr[i],arr[j] = arr[j],arr[i]
        # # now we have our array in increasing order of freqs
        # # now take up the top k elements
        # result = []
        # for i in range(len(arr)):
        #     if i<k:
        #         result.append(arr[i][0])
        # return result



        