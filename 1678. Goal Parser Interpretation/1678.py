class Solution:
    def interpret(self, command: str) -> str:
        s = command
        s = s.replace("()",'o')
        s = s.replace("(al)","al")
        return s