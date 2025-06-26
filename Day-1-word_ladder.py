# https://leetcode.com/problems/word-ladder/description/

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if beginWord == endWord or endWord not in wordList:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == ch:
                        continue
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in wordList:
                        wordList.remove(newWord)
                        queue.append((newWord, level + 1))
        return 0

        """
        This function finds the shortest transformation sequence from beginWord to endWord.
        It uses BFS (Breadth-First Search) to explore all valid transformations.

        Key points:
        - Each transformation changes exactly one letter.
        - Each transformed word must exist in the given wordList.
        - The goal is to reach endWord in the minimum number of transformations.

        Steps:
        1. Convert wordList to a set for faster lookup and removal.
        2. Initialize a queue for BFS with (beginWord, level=1).
        3. At each level, try changing each character of the word to 'a'-'z'.
        4. If the new word is in the wordList:
           - Remove it to mark as visited.
           - Add it to the queue with level incremented.
        5. If endWord is found, return the level.
        6. If the queue is exhausted and endWord not found, return 0.
        """
