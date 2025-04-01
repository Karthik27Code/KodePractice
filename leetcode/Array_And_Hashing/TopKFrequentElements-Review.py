from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = defaultdict(int)
        numHeap = []
        for num in nums:
            numDict[num] += 1

        for num, count in numDict.items():
            heapq.heappush(numHeap, (count*-1, num))

        output = []
        for i in range(k):
            count, num = heapq.heappop(numHeap)
            output.append(num)

        return output

solution = Solution()
print("Top 2 frequent element of list [1,1,1,2,2,3] is: ", solution.topKFrequent([1,1,1,2,2,3], 2))


#This problem can also be solved using quickselect. please complete the below implementation. Read approach 2 in leet code editorial: https://leetcode.com/problems/top-k-frequent-elements/editorial/#approach-2-quickselect-hoares-selection-algorithm.
class QuickSelectSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = defaultdict(int)
        numHeap = []
        for num in nums:
            numDict[num] += 1

        for num, count in numDict.items():
            heapq.heappush(numHeap, (count*-1, num))

        output = []
        for i in range(k):
            count, num = heapq.heappop(numHeap)
            output.append(num)

        return output