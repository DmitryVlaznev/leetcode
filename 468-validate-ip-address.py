# 468. Validate IP Address

# Write a function to check whether an input string is a valid IPv4
# address or IPv6 address or neither.

# IPv4 addresses are canonically represented in dot-decimal notation,
# which consists of four decimal numbers, each ranging from 0 to 255,
# separated by dots ("."), e.g.,172.16.254.1;

# Besides, leading zeros in the IPv4 is invalid. For example, the
# address 172.16.254.01 is invalid.

# IPv6 addresses are represented as eight groups of four hexadecimal
# digits, each group representing 16 bits. The groups are separated by
# colons (":"). For example, the address
# 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could
# omit some leading zeros among four hexadecimal digits and some
# low-case characters in the address to upper-case ones, so
# 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit
# leading zeros and using upper cases).

# However, we don't replace a consecutive group of zero value with a
# single empty group using two consecutive colons (::) to pursue
# simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid
# IPv6 address.

# Besides, extra leading zeros in the IPv6 is also invalid. For example,
# the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

# Note: You may assume there is no extra space or special characters in
# the input string.

# Example 1:
# Input: "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".

# Example 2:
# Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".

# Example 3:
# Input: "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def checkV4(part: str) -> bool:
            try:
                if len(part) > 3: return False
                digits = ["1","2","3","4","5","6","7","8","9"]
                if len(part) > 1 and part[0] not in digits: return False
                if int(part) > 255: return False
                return True
            except:
                return False

        def checkV6(part: str) -> bool:
            try:
                if len(part) > 4 or len(part) == 0: return False
                signs = ["+","-"]
                if part[0] in signs: return False
                int(part, 16)
                return True
            except:
                return False

        splitted = IP.split(".")
        if len(splitted) == 4 and all([checkV4(p) for p in splitted]): return "IPv4"
        splitted = IP.split(":")
        if len(splitted) == 8 and all([checkV6(p) for p in splitted]): return "IPv6"
        return "Neither"

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

print("------- check IPv4 -------")

log("IPv4", t.validIPAddress("172.16.254.1"))
log("Neither", t.validIPAddress("172.16.256.1"))
log("Neither", t.validIPAddress("172.16.25.1.8"))
log("Neither", t.validIPAddress("172.16.025.1"))
log("Neither", t.validIPAddress("172.16.+.1"))
log("Neither", t.validIPAddress("172.16.-.1"))
log("IPv4", t.validIPAddress("0.0.0.0"))
log("IPv4", t.validIPAddress("255.255.255.255"))

print("------- check IPv6 -------")
log("IPv6", t.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
log("IPv6", t.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334"))
log("Neither", t.validIPAddress("02001:db8:85a3:0:0:8A2E:0370:7334"))
log("Neither", t.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334:234"))
log("Neither", t.validIPAddress("2001:0db8:85a3::8A2E:0370:7334"))
log("Neither", t.validIPAddress("1081:db8:85a3:01:-0:8A2E:0370:7334"))
log("Neither", t.validIPAddress("1081:db8:85a3:+:0:8A2E:0370:7334"))
log("Neither", t.validIPAddress("1081:db8:85a3:#4:0:8A2E:0370:7334"))