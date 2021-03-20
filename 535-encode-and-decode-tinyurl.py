# 535. Encode and Decode TinyURL

# Medium

# Note: This is a companion problem to the System Design problem: Design
# TinyURL.

# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short
# URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is
# no restriction on how your encode/decode algorithm should work. You
# just need to ensure that a URL can be encoded to a tiny URL and the
# tiny URL can be decoded to the original URL.


class Codec:
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        import hashlib

        h = "https://ex.com/" + hashlib.md5(longUrl.encode("utf-8")).hexdigest()[0:8]
        counter = 1
        url = h
        while url in self.urls:
            url = h + str(counter)
            counter += 1
        self.urls[url] = longUrl
        return url

    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.urls:
            return self.urls[shortUrl]
        return None


t = Codec()
long = "https://leetcode.com/problems/design-tinyurl"
short = t.encode(long)
print(long)
print(short)
print(t.decode(short))