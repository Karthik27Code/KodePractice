from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        alpha = [0 for i in range(26)]

        #if both strings are not same length, then they can't be anagrams
        if slen != tlen:
            return False

        for i in range(slen):
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if alpha[i] != 0:
                return False

        return True
    

solution = Solution()
print("anagram and  nagaram are anagrams: ", solution.isAnagram("anagram", "nagaram"))