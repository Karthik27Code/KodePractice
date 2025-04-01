from collections import deque, defaultdict
from unittest import TestCase

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList:
            return 0
        
        wordQue = deque([(beginWord, 1)])
        similarWords = defaultdict(list)
        neighbors = defaultdict(list)
        visited = {}
        
        for word in wordList:
            for ind in range(len(word)):
                dictWord = word[:ind] + '*' + word[ind+1:]
                for neighbor in similarWords[dictWord]:
                    neighbors[neighbor].append(word)
                    neighbors[word].append(neighbor)

                similarWords[dictWord].append(word)

        for ind in range(len(beginWord)):
                dictWord = beginWord[:ind] + '*' + beginWord[ind+1:]
                for neighbor in similarWords[dictWord]:
                    neighbors[neighbor].append(beginWord)
                    neighbors[beginWord].append(neighbor)

                similarWords[dictWord].append(beginWord)

        while wordQue:
            currWord, transformLen = wordQue.popleft()

            if currWord in visited:
                continue

            visited[currWord] = True

            if currWord == endWord:
                return transformLen
            
            for neighbor in neighbors[currWord]:
                if neighbor not in visited:
                    wordQue.append((neighbor, transformLen+1))

        return 0


sol = Solution()
test = TestCase()

# sol.threeSum([-1,0,1,2,-1,-4])

test.assertEqual(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5, "Assert failed for input hit and cog")
test.assertEqual(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]), 0, "Assert failed for input hit and cog")    

# sampWord = "cog"
# for ind in range(len(sampWord)):
#     dictWord = sampWord[:ind] + '*' + sampWord[ind+1:]
#     print(dictWord)

        # Can we build a graph and do a BFS to find the shortest path?


# check the leetcode editorial for the bidirectional breadth first search : https://leetcode.com/problems/word-ladder/editorial/#approach-2-bidirectional-breadth-first-search 
