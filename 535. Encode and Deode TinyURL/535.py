import base64
class Codec:
    dic = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        k = longUrl
        k = k.encode("ascii")
        k = base64.b64encode(k)
        k = k.decode("ascii")
        self.dic[k] = longUrl
        return k

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))