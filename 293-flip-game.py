# 293. Flip Game

# Easy

# You are playing a Flip Game with your friend.

# You are given a string currentState that contains only '+' and '-'.
# You and your friend take turns to flip two consecutive "++" into "--".
# The game ends when a person can no longer make a move, and therefore
# the other person will be the winner.

# Return all possible states of the string currentState after one valid
# move. You may return the answer in any order. If there is no valid
# move, return an empty list [].

# Example 1:
# Input: currentState = "++++"
# Output: ["--++","+--+","++--"]

# Example 2:
# Input: currentState = "+"
# Output: []


# Constraints:
# 1 <= currentState.length <= 500
# currentState[i] is either '+' or '-'.

from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        arr = [s for s in currentState]
        res = []
        for i in range(len(arr) - 1):
            if arr[i] == "+" and arr[i + 1] == "+":
                res.append("".join(arr[:i] + ["-", "-"] + arr[i + 2 :]))
        return res
