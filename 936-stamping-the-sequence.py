# 936. Stamping The Sequence

# Hard

# You want to form a target string of lowercase letters.

# At the beginning, your sequence is target.length '?' marks.  You also
# have a stamp of lowercase letters.

# On each turn, you may place the stamp over the sequence, and replace
# every letter in the sequence with the corresponding letter from the
# stamp.  You can make up to 10 * target.length turns.

# For example, if the initial sequence is "?????", and your stamp is
# "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.
# (Note that the stamp must be fully contained in the boundaries of the
# sequence in order to stamp.)

# If the sequence is possible to stamp, then return an array of the
# index of the left-most letter being stamped at each turn.  If the
# sequence is not possible to stamp, return an empty array.

# For example, if the sequence is "ababc", and the stamp is "abc", then
# we could return the answer [0, 2], corresponding to the moves "?????"
# -> "abc??" -> "ababc".

# Also, if the sequence is possible to stamp, it is guaranteed it is
# possible to stamp within 10 * target.length moves.  Any answers
# specifying more than this number of moves will not be accepted.


# Example 1:
# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# ([1,0,2] would also be accepted as an answer, as well as some other answers.)

# Example 2:
# Input: stamp = "abca", target = "aabcaca"
# Output: [3,0,1]

# Note:
# 1 <= stamp.length <= target.length <= 1000
# stamp and target only contain lowercase letters.

from typing import List
from collections import deque


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s_len, t_len = len(stamp), len(target)

        dq = deque()
        done = [False] * t_len
        ans = []
        A = []
        for i in range(t_len - s_len + 1):
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i + j]
                if a == c:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            A.append((made, todo))

            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        dq.append(j)
                        done[j] = True
        while dq:
            i = dq.popleft()
            for j in range(max(0, i - s_len + 1), min(t_len - s_len, i) + 1):
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        ans.append(j)
                        for m in A[j][0]:
                            if not done[m]:
                                dq.append(m)
                                done[m] = True
        return ans[::-1] if all(done) else []


t = Solution()
print("--------------")
print(t.movesToStamp("abca", "aabcaca"))
# print("--------------")
# print(t.movesToStamp("aa", "aaaaaaa"))
