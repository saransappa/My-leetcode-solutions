class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            p = list(i)
            p.sort()
            z = ''.join(p)
            if d.get(z,0)==0:
                d[z]=""
            d[z] = d[z] + " "+i
        k = []
        for i in d.values():
            r = i.split(" ")
            r = r[1:]
            k.append(r)
        return k