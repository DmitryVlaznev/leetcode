# 127. Word Ladder

# Hard

# Given two words beginWord and endWord, and a dictionary wordList,
# return the length of the shortest transformation sequence from
# beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Return 0 if there is no such transformation sequence.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot"
# -> "dog" -> "cog", return its length 5.

# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no
# possible transformation.

# Constraints:
# 1 <= beginWord.length <= 100
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the strings in wordList are unique.

from typing import List
from utils import checkValue


class Solution:
    def neighbors(self, word, wordList, letters):
        res = []
        for i in range(len(word)):
            for l in letters:
                neighbor = word[0:i] + l + word[i + 1 :]
                if neighbor != word and neighbor in wordList:
                    res.append(neighbor)
        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        from collections import deque

        letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        dq = deque()
        dq.append(beginWord)
        seen, steps = set([beginWord]), 0
        while dq:
            l = len(dq)
            steps += 1
            while l:
                l -= 1
                cur = dq.popleft()
                if cur == endWord:
                    return steps
                for nxt in self.neighbors(cur, wordList, letters):
                    if not nxt in seen:
                        dq.append(nxt)
                        seen.add(nxt)
        return 0

    def ladderLength2(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        from collections import defaultdict
        from collections import deque

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1 :]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


t = Solution()

checkValue(5, t.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
checkValue(0, t.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
checkValue(0, t.ladderLength("hit", "cog", ["hot", "rtt", "lot", "cog"]))
checkValue(2, t.ladderLength("a", "c", ["a", "b", "c"]))