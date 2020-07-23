class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        z=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                z.append("FizzBuzz")
            elif i%3==0:
                z.append("Fizz")
            elif i%5==0:
                z.append("Buzz")
            else:
                z.append(str(i))
        return z