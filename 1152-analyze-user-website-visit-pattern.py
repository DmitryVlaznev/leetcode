# 1152. Analyze User Website Visit Pattern

# Medium

# We are given some website visits: the user with name username[i]
# visited the website website[i] at time timestamp[i].

# A 3-sequence is a list of websites of length 3 sorted in ascending
# order by the time of their visits.  (The websites in a 3-sequence are
# not necessarily distinct.)

# Find the 3-sequence visited by the largest number of users. If there
# is more than one solution, return the lexicographically smallest such
# 3-sequence.


# Example 1:
# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation:
# The tuples in this example are:
# ["joe", 1, "home"]
# ["joe", 2, "about"]
# ["joe", 3, "career"]
# ["james", 4, "home"]
# ["james", 5, "cart"]
# ["james", 6, "maps"]
# ["james", 7, "home"]
# ["mary", 8, "home"]
# ["mary", 9, "about"]
# ["mary", 10, "career"]
# The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
# The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
# The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
# The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
# The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.


# Note:
# 3 <= N = username.length = timestamp.length = website.length <= 50
# 1 <= username[i].length <= 10
# 0 <= timestamp[i] <= 10^9
# 1 <= website[i].length <= 10
# Both username[i] and website[i] contain only lowercase characters.
# It is guaranteed that there is at least one user who visited at least 3 websites.
# No user visits two websites at the same time.

from typing import List


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        tuples = []
        for i in range(len(username)):
            tuples.append((username[i], timestamp[i], website[i]))
        tuples.sort(key=lambda t: t[1])
        tuples.sort(key=lambda t: t[0])

        def get_3sequences(res, cur: List[str], rest: List[str]):
            if len(cur) == 3:
                res.add(" ".join(cur))
                return
            if not rest:
                return
            get_3sequences(res, cur.copy() + [rest[0]], rest[1:])
            get_3sequences(res, cur.copy(), rest[1:])

        def add_sequences(res, user_websites):
            sequences = set()
            get_3sequences(sequences, [], user_websites)
            for s in sequences:
                if s in res:
                    res[s] += 1
                else:
                    res[s] = 1

        res, user_websites = {}, [tuples[0][2]]
        for i, t in enumerate(tuples[1:]):
            if tuples[i][0] == t[0]:
                user_websites.append(t[2])
                continue
            add_sequences(res, user_websites)
            user_websites = [t[2]]

        add_sequences(res, user_websites)

        top = []
        top_count = 0

        for seq, count in res.items():
            if count == top_count:
                top.append(seq)
            elif count > top_count:
                top = [seq]
                top_count = count
        top.sort()
        return top[0].split(" ")


t = Solution()

username = [
    "joe",
    "joe",
    "joe",
    "james",
    "james",
    "james",
    "james",
    "mary",
    "mary",
    "mary",
]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = [
    "home",
    "about",
    "career",
    "home",
    "cart",
    "maps",
    "home",
    "home",
    "about",
    "career",
]
print(t.mostVisitedPattern(username, timestamp, website))


username = ["u1", "u1", "u1", "u2", "u2", "u2"]
timestamp = [1, 2, 3, 4, 5, 6]
website = ["a", "b", "a", "a", "b", "c"]
print(t.mostVisitedPattern(username, timestamp, website))

username = [
    "him",
    "mxcmo",
    "jejuvvtye",
    "wphmqzn",
    "uwlblbrkqv",
    "flntc",
    "esdtyvfs",
    "nig",
    "jejuvvtye",
    "nig",
    "mxcmo",
    "flntc",
    "nig",
    "jejuvvtye",
    "odmspeq",
    "jiufvjy",
    "esdtyvfs",
    "mfieoxff",
    "nig",
    "flntc",
    "mxcmo",
    "qxbrmo",
]
timestamp = [
    113355592,
    304993712,
    80831183,
    751306572,
    34485202,
    414560488,
    667775008,
    951168362,
    794457022,
    813255204,
    922111713,
    127547164,
    906590066,
    685654550,
    430221607,
    699844334,
    358754380,
    301537469,
    561750506,
    612256123,
    396990840,
    60109482,
]
website = [
    "k",
    "o",
    "o",
    "nxpvmh",
    "dssdnkv",
    "kiuorlwdcw",
    "twwginujc",
    "evenodb",
    "qqlw",
    "mhpzoaiw",
    "jukowcnnaz",
    "m",
    "ep",
    "qn",
    "wxeffbcy",
    "ggwzd",
    "tawp",
    "gxm",
    "pop",
    "xipfkhac",
    "weiujzjcy",
    "x",
]
#
["m", "kiuorlwdcw", "xipfkhac"]
print(t.mostVisitedPattern(username, timestamp, website))