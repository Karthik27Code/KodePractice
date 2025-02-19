from typing import List
from unittest import TestCase

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        end = len(nums) - 1
        total_cnt = 0
        while fast <= end and slow <= end:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                total_cnt += 1
                slow += 1

            fast += 1

        return total_cnt
    
sol = Solution()
test = TestCase()

test.assertEqual(sol.removeElement([3,2,2,3], 3), 2, "assert failed for input [3,2,2,3], 3.")
test.assertEqual(sol.removeElement([0,1,2,2,3,0,4,2], 2), 5, "assert failed for input [0,1,2,2,3,0,4,2], 2.")
    

