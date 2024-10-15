from typing import List
from unittest import TestCase

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        running_product = 1
        for idx, num in enumerate(nums):
            running_product *= num
            left_product[idx] = running_product

        running_product = 1
        for idx in range(len(nums) -1, -1, -1):
            running_product *= nums[idx]
            right_product[idx] = running_product

        output = []
        for idx in range(len(nums)):
            if idx == 0:
                output.append(right_product[idx+1])
            elif idx == len(nums) - 1:
                output.append(left_product[idx-1])
            else:
                output.append(left_product[idx-1] * right_product[idx+1])

        return output
    

#optimizing the solution to use O(1) space
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        running_product = 1
        for idx, num in enumerate(nums):
            output[idx] = running_product
            running_product *= num

        running_product = 1
        for idx in range(len(nums) -1, -1, -1):
            output[idx] *= running_product
            running_product *= nums[idx]

        return output
    

solution = Solution()
test = TestCase()
solution2 = Solution2()

# print(solution.productExceptSelf([1,2,3,4]))

test.assertCountEqual(solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
test.assertCountEqual(solution.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

test.assertCountEqual(solution2.productExceptSelf([1,2,3,4]), [24,12,8,6], f"failed for input [1,2,3,4]")
test.assertCountEqual(solution2.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0], f"failed for input [-1,1,0,-3,3]")