from unittest import TestCase

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
    
test = TestCase()
sol = Solution()

test.assertEqual(sol.findMin([3,4,5,1,2]), 1, "assert failed for input [3,4,5,1,2]")
