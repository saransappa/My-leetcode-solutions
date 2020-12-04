class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        punc = '''!()-[]{};:'"\,<>./?@#$%`^&*_~'''
        for i in punc:
            s = s.replace(i,"")
        if s==s[::-1]:
            return True
        else:
            return False