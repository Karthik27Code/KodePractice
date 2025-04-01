from typing import List
from unittest import TestCase

class Solution:
    def trap(self, height: List[int]) -> int:
        water_collected = [0] * len(height)

        left_max = 0
        for idx, h in enumerate(height):
            if left_max > h:
                water_collected[idx] = left_max - h
            else:
                left_max = h

        right_max = 0
        for idx in range(len(height)-1, -1, -1):
            h = height[idx]
            if right_max > h:
                water_collected[idx] = min(water_collected[idx], (right_max-h))
            else:
                right_max = h
                water_collected[idx] = 0

        total_collected = 0
        for wc in water_collected:
            total_collected += wc

        return total_collected
    

sol = Solution()
test = TestCase()

test.assertEqual(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6, "Assert failed for input [0,1,0,2,1,0,1,3,2,1,2,1]")
test.assertEqual(sol.trap([4,2,0,3,2,5]), 9, "Assert failed for input [4,2,0,3,2,5]")

# elevation at a point is calculated as follows:
    # let elevation at that point be - pe
    # highest point in the left side until that point - lh
    # highest point in the right side until that point - rh
    # water collected at that point = max(min(lh, rh) - pe, 0)
    #  We have to do this for all the points 


# There are more efficient ways to solve this problem. Please refer to the stack approach : https://leetcode.com/problems/trapping-rain-water/editorial/#approach-3-using-stacks
# More optimized approach with O(1) memory using two pointers : https://leetcode.com/problems/trapping-rain-water/editorial/#approach-4-using-2-pointers