from unittest import TestCase
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
        if nums[left] == target:
            return left
        
        return -1
    

sol = Solution()
test = TestCase()

test.assertEqual(sol.search([4,5,6,7,0,1,2], 0), 4, "assert failed for input [4,5,6,7,0,1,2] and target 0")
test.assertEqual(sol.search([4,5,6,7,0,1,2], 3), -1, "assert failed for input [4,5,6,7,0,1,2] and target 3")
test.assertEqual(sol.search([1], 0), -1, "assert failed for input [1] and target 0")
test.assertEqual(sol.search([3,1], 3), 0, "assert failed for input [3,1] and target 3")