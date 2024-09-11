from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        for i, num in enumerate(nums):
            reverseTarget = target - num
            if reverseTarget in numdict:
                return [numdict[reverseTarget], i]

            numdict[num] = i

        return []
    
solution = Solution()
print("two numbers from [2,7,11,15] for 9 are in position: ", solution.twoSum([2,7,11,15], 9))