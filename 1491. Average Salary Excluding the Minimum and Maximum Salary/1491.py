class Solution:
    def average(self, salary: List[int]) -> float:
        mi = min(salary)
        ma = max(salary)
        sum = 0
        k = 0
        for i in  salary:
            if i!=mi and i!=ma:
                sum+=i
                k+=1
        return sum/k