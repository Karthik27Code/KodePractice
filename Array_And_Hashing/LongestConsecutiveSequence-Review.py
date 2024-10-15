from typing import List
from unittest import TestCase

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            num_dict[num] = False

        max_len = 0
        for num in nums:
            if not num_dict[num]:
                length = 1
                #forward
                iter = num + 1
                while iter in num_dict:
                    length += 1
                    num_dict[iter] = True
                    iter += 1
                    
                #backward
                iter = num - 1
                while iter in num_dict:
                    length += 1
                    num_dict[iter] = True
                    iter -= 1

                max_len = max(max_len, length)

        return max_len
    

#This is optimized solution. Check out python sets and what is the difference between sets and dictionary.
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            num_dict[num] = False

        max_len = 0
        for num in nums:
            if num-1 not in num_dict:
                length = 1
                #forward
                iter = num + 1
                while iter in num_dict:
                    length += 1
                    iter += 1

                max_len = max(max_len, length)

        return max_len
    


test = TestCase()
sol = Solution()
sol2 = Solution2()

test.assertEqual(sol.longestConsecutive([100,4,200,1,3,2]), 4, f"assert failed for input [100,4,200,1,3,2]")
test.assertEqual(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9, f"assert failed for input [0,3,7,2,5,8,4,6,0,1]")

test.assertEqual(sol2.longestConsecutive([100,4,200,1,3,2]), 4, f"assert failed for input [100,4,200,1,3,2]")
test.assertEqual(sol2.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9, f"assert failed for input [0,3,7,2,5,8,4,6,0,1]")
            


# brute force - sort the array and traverse the list and check previous element to see if they are consecutive.
# we can try hashing - put all the numbers into an hash and mark as unvisited.
# for each number, search backward and forward and mark all the number visited.
# count the lenght and store the maximum length.