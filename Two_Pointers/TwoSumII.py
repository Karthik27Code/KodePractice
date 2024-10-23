from typing import List
from unittest import TestCase

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            num1 = numbers[start]
            num2 = numbers[end]
            sum = num1 + num2
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start+1, end+1]
        
        return []
    
sol = Solution()
test = TestCase()

test.assertCountEqual(sol.twoSum([2,7,11,15], 9), [1,2], "Assert failed for input [2,7,11,15]")
test.assertCountEqual(sol.twoSum([2,3,4], 6), [1,3], "Assert failed for input [2,3,4]")
test.assertCountEqual(sol.twoSum([-1,0], -1), [1,2], "Assert failed for input [-1,0]")
