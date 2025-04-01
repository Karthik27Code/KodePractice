from typing import List
from unittest import TestCase

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer, right_pointer = 0, len(height) - 1
        max_area = 0
        while left_pointer < right_pointer:
            area = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)

            max_area = max(area, max_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            elif height[left_pointer] > height[right_pointer]:
                right_pointer -= 1
            else:
                if height[left_pointer + 1] > height[right_pointer - 1]:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        return max_area
    

sol = Solution()
test = TestCase()

test.assertEqual(sol.maxArea([1,8,6,2,5,4,8,3,7]), 49, "Assert failed for test case [1,8,6,2,5,4,8,3,7].")
test.assertEqual(sol.maxArea([1,1]), 1, "Assert failed for test case [1,1].")


# we can solve this using two pointer
# start with left and right pointers.
# calculate the area between the two pointers as follows:
    # min(height[right_pointer], height[left_pointer]) * (right_pointer - left_pointer)
# increment the pointer which is pointing to the minimum element.


# Review the proof given in leetcode : https://leetcode.com/problems/container-with-most-water/editorial/#approach-2-two-pointer-approach
# proof links : https://leetcode.com/problems/container-with-most-water/solutions/6089/Anyone-who-has-a-O(N)-algorithm/comments/7268/
# clarification link : https://leetcode.com/problems/container-with-most-water/solutions/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm/