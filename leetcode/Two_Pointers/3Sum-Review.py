from typing import List
from unittest import TestCase

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []
        for idx in range(0, len(nums)-2, 1):
            if idx -1 > 0 and sorted_nums[idx-1] == sorted_nums[idx]:
                continue
            start = idx + 1
            end = len(nums)-1
            num = sorted_nums[idx]
            while start < end:
                sum = num + sorted_nums[start] + sorted_nums[end]
                if sum > 0:
                    end -=1
                elif sum < 0:
                    start += 1
                else:
                    output.append([num, sorted_nums[start], sorted_nums[end]])
                    start += 1
                    while sorted_nums[start] == sorted_nums[start-1] and start < len(nums)-1:
                        start += 1

                    end -= 1
                    while sorted_nums[end] == sorted_nums[end+1] and end > 0:
                        end -= 1

        return output
    

sol = Solution()
test = TestCase()

# sol.threeSum([-1,0,1,2,-1,-4])

test.assertCountEqual(sol.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]], "Assert failed for input [-1,0,1,2,-1,-4]")
test.assertCountEqual(sol.threeSum([0,1,1]), [], "Assert failed for input [0,1,1]")
test.assertCountEqual(sol.threeSum([0,0,0]), [[0,0,0]], "Assert failed for input [0,0,0]")

# review the approach 2 and approach 3 mentioned in leetcode editorial : https://leetcode.com/problems/3sum/editorial/#approach-2-hashset
# approach 3 link : https://leetcode.com/problems/3sum/editorial/#approach-3-no-sort-

        

# brute force - 3 loops. keep track of triplets in hash set, so we don't add duplicates - O(n^3).
# sort the array - o(n log(n)) - total run time would be O(n^2).