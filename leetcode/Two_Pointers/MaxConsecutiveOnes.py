from typing import List
from unittest import TestCase


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ind = 0
        list_end = len(nums) - 1
        max_cnt = 0
        cnt = 0
        while ind <= list_end:
            if nums[ind] == 1:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 0

            ind += 1
        
        return max_cnt
    
sol = Solution()
test = TestCase()

test.assertEqual(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]), 3, "assert failed for input [1,1,0,1,1,1].")
test.assertEqual(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]), 2, "assert failed for input [1,0,1,1,0,1].")