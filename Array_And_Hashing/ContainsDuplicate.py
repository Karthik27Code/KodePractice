from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrdict = {}
        for n in nums:
            if n in arrdict:
                return True
            else:
                arrdict[n] = 0

        return False
    

solution = Solution()
print("[1,2,3,1] contains duplicate: ", solution.containsDuplicate([1,2,3,1]))
print("[1,2,3,4] contains duplicate: ", solution.containsDuplicate([1,2,3,4]))
print("[1,1,1,3,3,4,3,2,4,2] contains duplicate: ", solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))