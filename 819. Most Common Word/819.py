class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = paragraph.replace('!',' ')
        paragraph = paragraph.replace('?',' ')
        paragraph = paragraph.replace("'",' ')
        paragraph = paragraph.replace(',',' ')
        paragraph = paragraph.replace(';',' ')
        paragraph = paragraph.replace('.',' ')
        s = paragraph.split()
        d = {}
        for i in s:
            if d.get(i,0)==0:
                d[i] = 1
            else:
                d[i]+=1
        l = []
        for k,v in d.items():
            z = []
            z.append(v)
            z.append(k)
            l.append(z)
        l.sort(reverse= True)
        print(l)
        for i in l:
            if i[1] not in banned:
                return i[1]
