# Ransom Note

# Given an arbitrary ransom note string and another string containing
# letters from all the magazines, write a function that will return true
# if the ransom note can be constructed from the magazines ; otherwise,
# it will return false.

# Each letter in the magazine string can only be used once in your
# ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote: return True

        note_hash = {}
        for l in ransomNote:
            if l in note_hash: note_hash[l] += 1
            else: note_hash[l] = 1

        for l in magazine:
            if l in note_hash:
                note_hash[l] -= 1
                if note_hash[l] < 1: del note_hash[l]
                if not note_hash: return True
        return False

t = Solution()

print("False = ", t.canConstruct("a", "b"))
print("False = ", t.canConstruct("aa", "ab"))
print("True = ", t.canConstruct("aa", "aab"))
print("True = ", t.canConstruct("", "aab"))
print("False = ", t.canConstruct("sdf", ""))