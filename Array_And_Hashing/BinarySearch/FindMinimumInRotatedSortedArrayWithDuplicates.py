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
            while nums[mid] == nums[right] and right > mid:
                right -= 1
            while nums[mid] == nums[left] and left < mid:
                left += 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
    
test = TestCase()
sol = Solution()

test.assertEqual(sol.findMin([3,4,5,1,2]), 1, "assert failed for input [3,4,5,1,2]")
test.assertEqual(sol.findMin([2,2,2,0,1]), 0, "assert failed for input [2,2,2,0,1]")
test.assertEqual(sol.findMin([5, 5, 5, 5, 0, 1, 5]), 0, "assert failed for input [2,2,2,0,1]")
