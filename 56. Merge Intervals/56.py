class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x:x[0])
        ans.append(intervals[0])
        for i in intervals:
            c = 0
            if i not in ans:
                #print(ans)
                for j in ans:
                    print(i,j)
                    if i[0]>j[1]:
                        if i[1]<j[1]:
                            i[1] = j[1]
                        elif i not in ans:
                            c+=1
                    elif i[0]>=j[0]:
                        if i[1]>=j[1]:
                            j[1] = i[1]
                            #print(j)
                    else:
                        c+=1
                    print(ans)
            if c==len(ans) and i not in ans:
                ans.append(i)

        return ans
    