from typing import List
from unittest import TestCase
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        list_end = len(nums) - 1
        sum = 0
        best_size = sys.maxsize
        while start <= list_end and end <= list_end:
            sum += nums[end]

            while sum > target:
                best_size = min(best_size, (end - start)+1)
                sum -= nums[start]
                start += 1

            if sum == target:
                best_size = min(best_size, (end - start)+1)

            end += 1 

        return 0 if best_size == sys.maxsize else best_size
    
sol = Solution()
test = TestCase()

test.assertEqual(sol.minSubArrayLen(7, [2,3,1,2,4,3]), 2, "assert failed for input 7, [2,3,1,2,4,3].")
test.assertEqual(sol.minSubArrayLen(4, [1,4,4]), 1, "assert failed for input 4, [1,4,4].")
test.assertEqual(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 0, "assert failed for input 11, [1,1,1,1,1,1,1,1].")

