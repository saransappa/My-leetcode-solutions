class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        k = datetime.date(year,month,day)
        return k.strftime("%A")