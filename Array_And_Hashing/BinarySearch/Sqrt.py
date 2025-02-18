from unittest import TestCase

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = 2
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            sqr_value = mid * mid
            if sqr_value < x:
                left = mid + 1
            elif sqr_value > x:
                right = mid - 1
            else:
                return mid

        return right
    
sol = Solution()
test = TestCase

print(sol.mySqrt(4))
print(sol.mySqrt(8))
print(sol.mySqrt(9))
print(sol.mySqrt(0))
print(sol.mySqrt(1))
print(sol.mySqrt(2))
print(sol.mySqrt(6))

# test.assertEqual(sol.mySqrt(4), 2, "assert failed for input 4.")
# test.assertEqual(sol.mySqrt(8), 2, "assert failed for input 8.")

