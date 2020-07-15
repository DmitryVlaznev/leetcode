class Solution:
    def reverseWords(self, s: str) -> str:
        p = 0
        words = []
        w = None
        while p < len(s):
            if s[p] == " " and w is not None:
                words.append(s[w:p])
                w = None
            elif s[p] != " " and w is None:
                w = p
            p += 1
        if w is not None:
            words.append(s[w:])
        words.reverse()
        return " ".join(words)
