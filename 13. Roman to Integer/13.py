class Solution:
    def romanToInt(self, s: str) -> int:
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        d['!'] = 4
        d['@'] = 9
        d['#'] = 40
        d['$'] = 90
        d['%'] = 400
        d['^'] = 900
        
        
        s = s.replace('IV','!')
        s = s.replace('IX','@')
        s = s.replace('XL','#')
        s = s.replace('XC','$')
        s = s.replace('CD','%')
        s = s.replace('CM','^')
        
        ans = 0
        for i in s:
            ans+=d[i]
        return ans