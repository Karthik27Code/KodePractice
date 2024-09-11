from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            #sortedWord = self.countLetters(word)
            if sortedWord in strDict:
                strDict[sortedWord].append(word)
            else:
                strDict[sortedWord] = [word]
        
        output = []
        for word, wordList in strDict.items():
            output.append(wordList)

        return output
    
    def countLetters(self, word: str) -> tuple:
        alpha = [0] * 26
        for char in word:
            alpha[ord(char) - ord('a')] += 1
        
        return tuple(alpha)
    
solution = Solution()
print("grouped anagrams: ", solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))