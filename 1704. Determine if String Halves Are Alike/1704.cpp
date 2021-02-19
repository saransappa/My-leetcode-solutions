class Solution:
    global vowel
    def vowel(self,s: str) -> int:
        z = 'aeiou'
        c = 0
        for i in s:
            if i in z:
                c+=1
        return c
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        #print(a,b)
        if vowel(self,a)==vowel(self,b):
            return True
        else:
            return False