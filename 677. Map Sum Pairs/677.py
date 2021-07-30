class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, key: str, val: int) -> None:
        self.dict[key] = val

    def sum(self, prefix: str) -> int:
        sum = 0
        for k,v in self.dict.items():
            if k.startswith(prefix):
                sum+=v
        return sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)