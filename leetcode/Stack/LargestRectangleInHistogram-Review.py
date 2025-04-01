from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for idx in range(len(heights)):
            cnter = idx-1
            left_cnt = 0
            #left check
            while cnter >= 0 and heights[cnter] >= heights[idx]:
                cnter -= 1
                left_cnt += 1

            cnter = idx+1
            right_cnt = 0
            #right check
            while cnter <= len(heights)-1 and heights[cnter] >= heights[idx]:
                cnter += 1
                right_cnt += 1

            area = (left_cnt + right_cnt + 1) * heights[idx]
            max_area = max(max_area, area)

        return max_area


# this solution is not optimal.
# Please check the leetcode editorial for divide and conquer approach : https://leetcode.com/problems/largest-rectangle-in-histogram/editorial/#approach-3-divide-and-conquer-approach
# Also check the stack approach: https://leetcode.com/problems/largest-rectangle-in-histogram/editorial/#approach-5-using-stack

# for every number check how many neighbors greater than it. break if any number less than it occurs on either side.
# total area is number multiplied by (the number of neighbors found + 1)
