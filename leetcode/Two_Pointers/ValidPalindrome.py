from unittest import TestCase

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1
            
            while not s[end].isalnum() and start < end:
                end -= 1

            if s[start].isalnum() and s[end].isalnum() and s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
            
        return True
    

sol = Solution()
test = TestCase()

test.assertEqual(sol.isPalindrome("A man, a plan, a canal: Panama"), True, "Assert failed for input 'A man, a plan, a canal: Panama'")
test.assertEqual(sol.isPalindrome("race a car"), False, "Assert failed for input 'race a car'")
test.assertEqual(sol.isPalindrome(" "), True, "Assert failed for input ' '")
test.assertEqual(sol.isPalindrome("0P"), False, "Assert failed for input '0P'")




# test cases:
# what happens inner while loop causes the 'start < end' condition to fail
# lets assume end and start traversed 'i' characters and all are equal.
# lets say (len(s) - 1 - i) - 1  is the next character which is pointed by end.
# lets say i is the next non-character pointed by start and the remaining are also non characters.
# in this scenario we have i matching characters and one center character, so this is still a valid palindrome.