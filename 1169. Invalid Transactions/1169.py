class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        names = []
        for i in transactions:
            z = i.split(',')
            names.append(z[0])
            #if int(z[2])>1000:
                #invalid.append(i)

        for i in transactions:
            if i not in invalid:
                z = i.split(',')
                name =  z[0]
                time = int(z[1])
                if int(z[2])>1000:
                    invalid.append(i)
                    continue
                for j in transactions:
                    y = j.split(',')
                    if y[0]==name and abs(time-int(y[1]))<=60 and y[3]!=z[3]:
                        invalid.append(j)
                        invalid.append(i)
        return list(set(invalid))
            